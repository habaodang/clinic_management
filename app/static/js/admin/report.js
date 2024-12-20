document.addEventListener('DOMContentLoaded', function () {
  const ctx = document.getElementById('revenueChart').getContext('2d');
  const revenueChart = new Chart(ctx, {
    type: 'bar', // Loại biểu đồ: 'bar' cho biểu đồ cột
    data: {
      labels: ['Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5', 'Tháng 6', 'Tháng 7', 'Tháng 8', 'Tháng 9', 'Tháng 10', 'Tháng 11', 'Tháng 12'],
      datasets: [{
        label: 'Doanh Thu (triệu đồng)',
        data: [75, 100, 90, 110, 85, 95, 105, 115, 80, 125, 120, 130], // Dữ liệu mẫu
        backgroundColor: 'rgba(54, 162, 235, 0.5)', // Màu nền cột
        borderColor: 'rgba(54, 162, 235, 1)', // Màu viền cột
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'top',
        },
        tooltip: {
          callbacks: {
            label: function(context) {
              let value = context.raw;
              return ' Doanh Thu: ' + value + ' triệu đồng';
            }
          }
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          title: {
            display: true,
            text: 'Doanh Thu (triệu đồng)'
          }
        },
        x: {
          title: {
            display: true,
            text: 'Tháng'
          }
        }
      }
    }
  });
});
