import requests

template_id_var = ["PoP_kyivstarTV_activation_Base_completed",
"PoP_kyivstarTV_activation_Packallchannels_completed",
"PoP_kyivstarTV_Packallchannels_3days_before_expiration",
"PoP_kyivstarTV_activation_Adult_completed",
"PoP_kyivstarTV_activation_KinoHit_completed",
"PoP_kyivstarTV_activation_Light_completed",
"PoP_kyivstarTV_activation_Lightstart_completed",
"PoP_kyivstarTV_Lightstart_3days_before_expiration",
"PrP_kyivstarTV_activation_PremiumHD_completed",
"PrP_kyivstarTV_activation_Packallchannels_completed",
"PrP_kyivstarTV_Packallchannels_3days_before_expiration",
"PrP_kyivstarTV_activation_Adult_completed",
"PrP_kyivstarTV_activation_KinoHit_completed",
"PrP_kyivstarTV_activation_Light_completed",
"PrP_kyivstarTV_activation_Lightstart_completed",
"PrP_kyivstarTV_Lightstart_3days_before_expiration",
"PrP_kyivstarTV_activation_Basic2021_completed",
"PrP_kyivstarTV_activation_Family2021_completed",
"PrP_kyivstarTV_Family2021_3days_before_expiration",
"PrP_kyivstarTV_activation_PremiumHD2021_completed",
"PrP_kyivstarTV_activation_PremiumHD2021_50_completed",
"PrP_kyivstarTV_PremiumHD2021_3days_before_expiration",
"PrP_kyivstarTV_activation_LightStart2021_completed",
"PrP_kyivstarTV_LightStart2021_3days_before_expiration",
"FTTB_kyivstarTV_activation_Family2021_completed",
"FTTB_kyivstarTV_Family2021_3days_before_expiration",
"FTTB_kyivstarTV_PremiumHD2021_3days_before_expiration",
"FTTB_kyivstarTV_activation_Basic2021_completed",
"FTTB_kyivstarTV_activation_PremiumHD2021_completed",
"PoP_kyivstar_TV_family_successful_connection",
"PoP_kyivstar_TV_premium_HD_successful_connection",
"PoP_kyivstar_TV_premium_HD_50uah_with_disc_3mos",
"PrP_kyivstarTV_activation_Family2021_3_completed",
"PrP_kyivstarTV_activation_Family2021_6_completed",
"PrP_kyivstarTV_activation_Family2021_12_completed",
"PrP_kyivstarTV_activation_PremiumHD2021_3_completed",
"PrP_kyivstarTV_activation_PremiumHD2021_6_completed",
"PrP_kyivstarTV_activation_PremiumHD2021_12_completed",
"PrP_kyivstarTV_activation_Kids_completed",
"fttb_kyivstarTV_activation_Kids_completed",
"PoP_New_tariffs_national_inform_about_conditions_connected_to_allTP",
"LOVEUA_sms_connecting_RPLOVE",
"Pop_LOVEUA_Base_migration",
"Pop_LOVEUA_Freedom_migration",
"Pop_LOVE_forParents_migration",
"Pop_LOVE_forParentsHome_migration",
"POP_kyivstar_family_TP_activation",
"POP_activation_TP_simple",
"POP_activation_TP_kyivstar_online_plus_MMC",
"POP_Gaming_tariff_inform_conditions",
"PoP_New_tariffs_national_inform_about_conditions_connected_to_VASH_start_Vybir",
"PoP_New_tariffs_national_inform_about_conditions_connected_to_VASH_Vybir",
"PoP_New_Regional_inform_about_conditions_connected_to_allTP",
"PoP_callforparents_welcome_SMS",
"PoP_internetforparents_welcome_SMS",
"Login_to_activationpage",
"fttb_TP_activation_HMINHOME2022_LS",
"fttb_TP_activation_HMINHOME2022",
"fttb_TP_activation_HMINHOMEBASE",
"PONTISDISC_20_PrP_connect_completed",
"PONTISDISC_40_PrP_connect_completed",
"PONTISDISC_60_PrP_connect_completed",
"PONTISDISC_20_PrP_connect_failed_techissue",
"PONTISDISC_40_PrP_connect_failed_techissue",
"PONTISDISC_60_PrP_connect_failed_techissue",
"PONTISDISC_PrP_20_disconnect_completed",
"PONTISDISC_PrP_40_disconnect_completed",
"PONTISDISC_PrP_60_disconnect_completed",
"PONTISDISC_PrP_20_disconnect_failed_techissue",
"PONTISDISC_PrP_40_disconnect_failed_techissue",
"PONTISDISC_PrP_60_disconnect_failed_techissue",
"PONTISDISC_PrP_20_reinform_1days_before_disconnecting",
"PONTISDISC_PrP_40_reinform_1days_before_disconnecting",
"PONTISDISC_PrP_60_reinform_1days_before_disconnecting",
"PONTISDISC_50_PrP_FMC_connect_completed",
"PONTISDISC_50_PrP_FMC_connect_failed_techissue",
"PONTISDISC_50_PrP_FMC_disconnect_completed",
"PONTISDISC_50_PrP_FMC_disconnect_failed_techissue",
"PONTISDISC_50_PrP_FMC_reinform_1days_before_disconnecting",
"PONTISDISC_PoP_connect_completed",
"PONTISDISC_40_PoP_connect_completed",
"PONTISDISC_60_PoP_connect_completed",
"PONTISDISC_PoP_connect_failed_techissue",
"PONTISDISC_40_PoP_connect_failed_techissue",
"PONTISDISC_60_PoP_connect_failed_techissue",
"PONTISDISC_PoP_disconnect_completed",
"PONTISDISC_40_PoP_disconnect_completed",
"PONTISDISC_60_PoP_disconnect_completed",
"PONTISDISC_PoP_disconnect_failed_techissue",
"PONTISDISC_40_PoP_disconnect_failed_techissue",
"PONTISDISC_60_PoP_disconnect_failed_techissue",
"PONTISDISC_PoP_reinform_1days_before_disconnecting",
"PONTISDISC_40_PoP_reinform_1days_before_disconnecting",
"PONTISDISC_60_PoP_reinform_1days_before_disconnecting",
"discount_25_75_100_activation",
"discount_25_75_100_expiration",
"discount_FMC_10_activation",
"discount_FMC_10_expiration"]
recipient_msisdn_var = "380981402174"
class MessageSender:
    def __init__(self, url_post, headers_post):
        self.url_post = url_post
        self.headers_post = headers_post

    def send_message(self, data_post):
        response = requests.post(self.url_post, headers=self.headers_post, json=data_post)
        return response

class ResponseHandler:
    def __init__(self, response):
        self.response = response

    def get_status(self):
        response_data = self.response.json().get('data', {})
        status = response_data.get('attributes', {}).get('status')
        return status

url_post = "https://2eab44fc-e0a2-4c43-9c55-d4bbc627e72c.mock.pstmn.io/api/v1/messages/"
headers_post = {
    "Content-Type": "application/json",
    "User-Agent": "PostmanRuntime/7.32.3",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br"
}

message_sender = MessageSender(url_post, headers_post)

for template_id in template_id_var:
    data_post = {
        "data": {
            "type": "messages",
            "attributes": {
                "request-id": "69099001-7dc3-11e7-80c3-005565f",
                "originator": "oleksii.kariaka",
                "language": "ukr",
                "sms-recipient": recipient_msisdn_var,
                "template-id": template_id,
                "params": {
                    "recipient_msisdn": recipient_msisdn_var
                }
            }
        }
    }

    response = message_sender.send_message(data_post)
    response_handler = ResponseHandler(response)
    status = response_handler.get_status()

    if status is not None:
        print(f"Статус для template-id '{template_id}': {status}")
    else:
        print(f"Статус не найден в ответе для template-id '{template_id}'")
    print(response.json())