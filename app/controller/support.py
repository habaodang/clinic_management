from flask import Flask, request, jsonify

# Cơ sở dữ liệu triệu chứng và khoa khám bệnh
# symptom_database = {
#     "ho": "Tai Mũi Họng",
#     "sốt": "Nội tổng quát",
#     "đau họng": "Tai Mũi Họng",
#     "khó thở": "Tim mạch",
#     "đau ngực": "Tim mạch",
#     "đau bụng": "Tiêu hóa",
#     "tiêu chảy": "Tiêu hóa",
#     "đau đầu": "Thần kinh",
#     "chóng mặt": "Thần kinh",
#     "ngứa": "Da liễu",
#     "đau khớp": "Cơ xương khớp",
# }
#
#
# def chat():
#     if request.method == 'POST':
#         user_input = request.form.get("message", "").lower()
#
#         # Kiểm tra nếu tin nhắn của người dùng có chứa triệu chứng
#         for symptom, department in symptom_database.items():
#             if symptom in user_input:
#                 # Trả về phản hồi JSON
#                 return jsonify({"reply": f"Dựa trên triệu chứng của bạn, bạn nên khám ở khoa {department}.", "user_input": user_input})
#
#         # Nếu không có triệu chứng phù hợp
#         return jsonify({"reply": "Xin lỗi, tôi không xác định được khoa phù hợp. Bạn nên đến khoa Nội tổng quát để được kiểm tra chi tiết.", "user_input": user_input})
#
#     # Nếu phương thức GET, trả về một phản hồi mặc định
#     return jsonify({"reply": None})

