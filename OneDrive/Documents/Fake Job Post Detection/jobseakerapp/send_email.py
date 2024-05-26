from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

SENDEREMAIL = "clientproject31@gmail.com"

def sendmail(username,userid, pwd, subject):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = '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'
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    html_content = "<html><body style='font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px;'><div style='max-width: 600px; margin: 0 auto; background-color: #fff; padding: 30px; border-radius: 10px; box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.1);'><center><a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/Y07Mv88s/jobchecker.png' border='0' alt='JobLink' style='display: block; margin: 0 auto; max-width: 200px; margin-bottom: 20px;'/></a><h2 style='text-align: center; color: #555;'>Welcome to Job Checker Platform</h2></center><p style='font-size: 16px; line-height: 1.6;'>Dear "+str(username)+",</p><p style='font-size: 16px; line-height: 1.6;'>Congratulations! Your registration as a Job Seeker has been successfully completed.</p><p style='font-size: 16px; line-height: 1.6;'>Below are your Email Id and password:</p><table style='width: 100%; border-collapse: collapse; margin-bottom: 20px;'><tr><td style='padding: 10px; border: 1px solid #555; font-weight: bold;'>Email ID:</td><td style='padding: 10px; border: 1px solid #555;'>"+str(userid)+"</td></tr><tr><td style='padding: 10px; border: 1px solid #555; font-weight: bold;'>Otp Code:</td><td style='padding: 10px; border: 1px solid #555;'>"+str(pwd)+"</td></tr></table><p style='font-size: 16px; line-height: 1.6;'>Please keep this information secure and do not share it with anyone.</p><p style='font-size: 16px; line-height: 1;'>Best regards,</p><p style='font-size: 16px; line-height: 1; color: blue'><b>The JobChecker Team</b></p></div></body></html>"
    sender = {"name":"Otp Verification","email":SENDEREMAIL}
    to = [{"email":str(userid),"name":userid}]
    reply_to = {"email":SENDEREMAIL,"name":"Otp Verification"}
    headers = {"Some-Custom-Name":"unique-id-1234"}
    params = {"parameter":"My param value","subject":subject}
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, reply_to=reply_to, headers=headers, html_content=html_content, sender=sender, subject=subject)

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)