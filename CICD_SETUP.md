# GitHub Actions CI/CD Setup

This document describes the CI/CD pipeline setup for the Clinic Management Flask application.

## Overview

The CI/CD pipeline automatically builds, tests, and deploys the application to a VMware ESXi VM whenever code is pushed to the main branch.

## Workflow Stages

### 1. Build and Test Stage
- Sets up Python 3.13 environment
- Installs dependencies
- Runs code linting with flake8
- Executes tests with pytest
- Builds Docker image
- Tests Docker image functionality

### 2. Deploy Stage (main branch only)
- Connects to VM via SSH
- Creates backup of current deployment
- Pulls latest code from GitHub
- Rebuilds and restarts Docker containers
- Performs health checks
- Implements rollback on failure

## Required GitHub Secrets

Configure the following secrets in your GitHub repository settings:

### SSH Configuration
- `SSH_PRIVATE_KEY`: Private SSH key for connecting to the VM
- `VM_HOST`: VM IP address (192.168.202.157)
- `VM_USER`: SSH username for the VM

### Application Configuration
- `DB_PASSWORD`: MySQL root password for production
- `SECRET_KEY`: Flask secret key for production

## VM Setup Requirements

### 1. Directory Structure
```bash
sudo mkdir -p /opt/clinic_management
sudo chown $USER:$USER /opt/clinic_management
cd /opt/clinic_management
git clone https://github.com/habaodang/clinic_management.git .
```

### 2. Docker and Docker Compose
Ensure Docker and Docker Compose are installed:
```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER

# Install Docker Compose (if not included with Docker)
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

### 3. SSH Key Setup
```bash
# On your local machine, generate SSH key pair
ssh-keygen -t rsa -b 4096 -f ~/.ssh/clinic_vm_key

# Copy public key to VM
ssh-copy-id -i ~/.ssh/clinic_vm_key.pub user@192.168.202.157

# Add private key content to GitHub Secrets as SSH_PRIVATE_KEY
cat ~/.ssh/clinic_vm_key
```

### 4. Firewall Configuration
```bash
# Allow SSH access
sudo ufw allow ssh

# Allow application port
sudo ufw allow 5000

# Enable firewall
sudo ufw enable
```

## Local Development

### 1. Environment Setup
```bash
# Copy environment template
cp .env.example .env.prod

# Edit with your configuration
nano .env.prod
```

### 2. Run with Docker Compose
```bash
# Development
docker compose up -d

# Production
docker compose -f docker-compose.yml --env-file .env.prod up -d
```

### 3. Run Tests
```bash
# Install test dependencies
pip install pytest pytest-cov flake8

# Run tests
pytest tests/ -v --cov=app

# Run linting
flake8 . --count --max-line-length=127 --statistics
```

## Health Checks

The application includes a health check endpoint at `/health` that returns:
```json
{
  "status": "healthy",
  "service": "clinic_management"
}
```

## Monitoring and Logs

### View Application Logs
```bash
# On the VM
sudo docker compose logs -f web

# View all services
sudo docker compose logs -f
```

### Monitor Container Status
```bash
sudo docker compose ps
```

## Troubleshooting

### Common Issues

1. **Health Check Failures**
   - Check if the application is binding to 0.0.0.0:5000
   - Verify database connection
   - Check container logs

2. **SSH Connection Issues**
   - Verify SSH key format in GitHub Secrets
   - Check VM firewall settings
   - Ensure SSH service is running

3. **Database Connection Issues**
   - Verify MySQL container is healthy
   - Check environment variables
   - Ensure database initialization completed

### Manual Rollback
```bash
# On the VM, if automatic rollback fails
cd /opt/clinic_management
sudo docker compose down

# Restore from backup
latest_backup=$(ls -t ../clinic_management_backup_* | head -1)
sudo cp -r "$latest_backup"/* .
sudo docker compose -f docker-compose.yml --env-file .env.prod up -d
```

## Security Considerations

1. **SSH Keys**: Use dedicated SSH keys for CI/CD, rotate regularly
2. **Secrets Management**: Never commit secrets to repository
3. **Network Security**: Configure firewall to allow only necessary ports
4. **Database Security**: Use strong passwords, consider encryption
5. **Container Security**: Keep base images updated, run as non-root user

## Performance Optimization

1. **Image Caching**: Multi-stage builds and layer optimization
2. **Volume Persistence**: Database data persisted in Docker volumes
3. **Health Checks**: Proper startup and readiness probes
4. **Resource Limits**: Configure appropriate memory and CPU limits

## Support

For issues with the CI/CD pipeline:
1. Check GitHub Actions logs
2. Review VM system logs
3. Verify all secrets are configured correctly
4. Ensure VM meets all requirements