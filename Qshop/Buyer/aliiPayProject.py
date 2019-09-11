from alipay import AliPay

alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnIIYur27kzgkV51p14bNhr/lN8eDUIIOc1+189LCo8rLNb9WYC8q+RypvFFf1uiK8ujeu+1ynLR0OBGwBgx1vzsWyfsg97XeHobfwbrPUmUI9jbYFsk6UD+7eZl7TfAL/ERmpCkJWliKIEcSWWAcD4uxDT/baZ+6hoRja4nH4tBCBzBPWYh4Qut9E0t7jMKCCd46SU7M4WNcOInlRTzu6mfF8LqRhXyGMt2oIj916W9B1eiFHiJ+61/rEghm0Li4kv4vNnac52IE04TXy+8CtksWJ47DFTOcYH2u8wFOBSU3GY2wKzI7yogIzwHgLqK5GT7wkHAQckpn70qazjr2tQIDAQAB
-----END PUBLIC KEY-----"""

alipay_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAnIIYur27kzgkV51p14bNhr/lN8eDUIIOc1+189LCo8rLNb9WYC8q+RypvFFf1uiK8ujeu+1ynLR0OBGwBgx1vzsWyfsg97XeHobfwbrPUmUI9jbYFsk6UD+7eZl7TfAL/ERmpCkJWliKIEcSWWAcD4uxDT/baZ+6hoRja4nH4tBCBzBPWYh4Qut9E0t7jMKCCd46SU7M4WNcOInlRTzu6mfF8LqRhXyGMt2oIj916W9B1eiFHiJ+61/rEghm0Li4kv4vNnac52IE04TXy+8CtksWJ47DFTOcYH2u8wFOBSU3GY2wKzI7yogIzwHgLqK5GT7wkHAQckpn70qazjr2tQIDAQABAoIBABa/ukR6i6dMg8vQb7AKQhmSDwlakLXFEcCnatU0D2KreXoog6+ba42mIu3ijiG4z2mbe7SpQP2SJUp5F7LpYLwZJKjbPeGDp/Ob+y43ryb01KalNiepvDYp7WAxdQDRIYzbjGfUJy3grMMgUYR4OdvwnB2m6Iej1gLzf1gEQO+wx5Q3b8J3OQPf4iLlDggpzx4KnGQlUUnRyWrH3qqsnF+DY5HPPc5P2BwHCfsFmmolVwSBqoRoXB8tFCZMXI6s8/R+TcHtLOdPM8bOEGwqHpS+wFRDEKFXqb5/nMaW+udNfYvsEflGEReqSMZsyzXbxueYNaCLwVyIoM80872HH8kCgYEAzGzOiLKnEZVCX7zR4YJqIMuNe1goHQHjLZFynIovNdz3bFMfXlmy8Xd3WJfx0PKZrKZVPG7opZRoeJMCD6Hx2O/0wN9KcS60aCaiNZJnSKTMrovQjUqyKxALK0DiRKSL8JdTHq+qr9E25Mwc9DVdvUvqVFdNCvUh9hNti5/rsR8CgYEAw/58iv6fvETUHMeHLMrfoNS1Z1Ahit025Bbnu3eepu+rSDkTjRpUL1BNsa6KVzK3POHyA3SeEvg7IjbGMlZ0rS7GFBeQY0iOyRIYq7tesoU6+e+bCQIgZiFhtf+GPucC0B5SfSE7e+kaF1yOjyJOXnIlAsDdvkP4hP9X5qRseasCgYEAmyDytk+EctZmsQoz50K1UL/HVNO4VRLql9jpNZuzadeONzj48/tzzMPQ4H0lt19yeM8cnai4iXaOtPkyNjS5t9uYS4jnD+7WXrb6n1bDZCATZ12YXLBTdlRNdXxeeKK5w1DCdeXuzE8irguq6TNaOF1UrL43K9qL9BYYKj2oeRcCgYAIT5NCZZeqaRTBf6h4usWO0VY74kb513WLaHk9Fs5wb7tInbr5gcNOGk6hGTCej/T7LO2RPfGyBjqjscTnv4jFCzW1BmbF/v6nAhBvv8s9MK8WiBV/5Uowanv1NreflTYmUxLWYYFfOLw1f2RAJ4lBMf/lxP3iIom4QgedLR24bwKBgQCuc0zxttiMSrWHBHtJDOo9pJV3rSngl1iMELqe197LIm7946M5IFmCL6hJcoOo4oudiV0vbAHD9ndrrZrrXNPnL2s79O6appFCG7y3yJS49slTSdqVYnSn8T1yS+7/l3c/pWgaz6j6KP7nUcgsgkSPJBo7B7KTr+gGz31cVsjFzQ==
-----END RSA PRIVATE KEY-----"""

# 实例化支付

alipay = AliPay(
    appid = "2016101200667714",
    app_notify_url = None,
    app_private_key_string=alipay_private_key_string,
    alipay_public_key_string = alipay_public_key_string,
    sign_type="RSA2"
)

order_string = alipay.api_alipay_trade_page_pay(
    out_trade_no = "1000000001",#订单编号
    total_amount = str(100), # 金额
    subject = "生鲜交易",
    return_url = None,
    notify_url = None
)

result = "https://openapi.alipaydev.com/gateway.do?" + order_string

print(result)