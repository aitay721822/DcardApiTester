
class APIResourse:
    # DCARD HOST NAME
    dcardHostName = 'https://www.dcard.tw'

    # DCARD PING POSITION
    # [METHOD,POSITION]
    dcardPing = ['GET','/_api/_ping']

    # DCARD LOGIN ENTRY POSITION
    # [METHOD,POSITION]
    dcardLogin = ['POST','/_api/sessions']

    # DCARD FORUM POST INFORMATION POSITION
    # [METHOD,POSITION]
    dcardForum = ['GET','/_api/posts']

    # DCARD LOGOUT ENTRY POSITION
    # [METHOD,POSITION]
    dcardLogout = ['GET','/logout']

    # DCARD ME INFOMATION POSITION
    # [METHOD,POSITION]
    dcardJsonMe = ['GET','/_api/me']
