# import requests
# import openpyxl
# import json
#
#
# class MessageSender:
#     def __init__(self, url_post, headers_post):
#         self.url_post = url_post
#         self.headers_post = headers_post
#         self.session = requests.Session()
#
#     def send_message(self, data_post):
#         response = self.session.post(self.url_post, headers=self.headers_post, json=data_post)
#         return response
#
#
# class ResponseHandler:
#     def __init__(self, response):
#         self.response = response
#
#     def get_status(self):
#         response_data = self.response.json().get('data', {})
#         status = response_data.get('attributes', {}).get('status')
#         return status
#
#
# def load_json(file_path):
#     with open(file_path, 'r') as json_file:
#         return json.load(json_file)
#
#
# def load_excel_template_content(file_path):
#     workbook = openpyxl.load_workbook(file_path)
#     sheet = workbook.active
#
#     template_content_dict = {}
#     header_row = list(sheet.iter_rows(min_row=1, max_row=1, values_only=True))[0]
#
#     template_id_col_idx = header_row.index("Template Id")
#     content_col_idx = header_row.index("sms-content-ukr")
#
#     for row in sheet.iter_rows(min_row=2, values_only=True):
#         template_id = row[template_id_col_idx]
#         content = row[content_col_idx]
#         template_content_dict[template_id] = content
#
#     return template_content_dict
#
#
# def main():
#     data = load_json('credentials.json')
#
#     msisdn = data.get('msisdn')
#     template_id_list_from_json = data.get('template_id')
#
#     template_id_var = template_id_list_from_json
#     recipient_msisdn_var = msisdn
#
#     url_post = "https://2eab44fc-e0a2-4c43-9c55-d4bbc627e72c.mock.pstmn.io/api/v1/messages/"
#     headers_post = {
#         "Content-Type": "application/json",
#         "User-Agent": "PostmanRuntime/7.32.3",
#         "Accept": "*/*",
#         "Accept-Encoding": "gzip, deflate, br"
#     }
#
#     message_sender = MessageSender(url_post, headers_post)
#
#     for template_id in template_id_var:
#         data_post = {
#             "data": {
#                 "type": "messages",
#                 "attributes": {
#                     "request-id": "69099001-7dc3-11e7-80c3-005565f",
#                     "originator": "oleh.bovkun",
#                     "language": "ukr",
#                     "sms-recipient": recipient_msisdn_var,
#                     "template-id": template_id,
#                     "params": {
#                         "recipient_msisdn": recipient_msisdn_var
#                     }
#                 }
#             }
#         }
#
#         response = message_sender.send_message(data_post)
#         response_handler = ResponseHandler(response)
#         status = response_handler.get_status()
#
#         if status is not None:
#             print("Статус код 202 - успешно")
#             print(f"СМС с темплейтом {template_id} было отправленно")
#             print("Статус:", status)
#             print("################################################################################")
#         else:
#             print("Статус не найден в ответе.")
#
#     url_get = "https://2eab44fc-e0a2-4c43-9c55-d4bbc627e72c.mock.pstmn.io/api/v1/messages?filter%5Brecipient-msisdn%5D=380981403355"
#     headers_get = {
#         "User-Agent": "PostmanRuntime/7.32.3",
#         "Accept": "*/*",
#         "Accept-Encoding": "gzip, deflate, br"
#     }
#
#     response_get = requests.get(url_get, headers=headers_get)
#     response_get_json = response_get.json()
#
#     if response_get.status_code == 200:
#         print("Запрос GET SMS успешен - 200")
#     else:
#         print("Ошибка запроса")
#
#     content_sms_list = {}
#     for item in response_get_json.get("data", []):
#         attributes = item.get("attributes", {})
#         payloads = attributes.get("payloads", [])
#         for payload in payloads:
#             template_id = payload.get("template-id")
#             if template_id in template_id_var:
#                 content = payload.get("content")
#                 content_sms_list[template_id] = content
#
#     print(content_sms_list)
#
#     template_content_dict = load_excel_template_content('Template_Test.xlsx')
#
#     common_template_ids = set(content_sms_list.keys()) & set(template_content_dict.keys())
#
#     for template_id in common_template_ids:
#         content_sms = content_sms_list.get(template_id)
#         content_template = template_content_dict.get(template_id)
#
#         print(f"Template ID: {template_id}")
#         print(f"Content from API: {content_sms}")
#         print(f"Content from Excel: {content_template}")
#         if content_sms == content_template:
#             print('Тексты совпадают!!!!')
#         else:
#             print('Тексты НЕ совпадают :(')
#         print("################################################################################")
#
#
# if __name__ == "__main__":
#     main()
#
