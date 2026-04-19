MOCK_EMAILS = [
        {"id": "msg_001",
            "threadId": "msg_001", "labelIds": ["INBOX", "UNREAD"],"snippet": "I have asked for a refund...",
            "internalDate": "1740038100000","payload": {
                "headers": [
                    {"name": "Subject", "value": "URGENT: REFUND REQUEST - ORDER #998822"},
                    {"name": "From", "value": "angry.customer@example.com"},
                    {"name": "To", "value": "support@techcompany.com"},
                    {"name": "Date", "value": "Thu, 20 Feb 2026 09:15:00 +0000"}
                ]
            },
            "body_text_content": """
            <div><b>URGENT:</b> Please &nbsp; read this!</div>

            I have asked for a refund three times now! Your service is not working.
            I expect a call at +1 (555) 010-9988 or email me at admin@personal.net.

            Check my status here: https://portal.techcompany.com/orders/998822

            > On Mon, Feb 10, 2026 at 9:00 AM, Support wrote:
            > > We are looking into your request.

            ---------- Forwarded message ---------
            From: Billing <billing@techcompany.com>
            Date: Feb 09, 2026
            Subject: Invoice #998822

            -- 
            Sent from my iPhone

            This email and any attachments are confidential and intended solely for the use of the individual...
            """
        },
        {"id":"msg_002","threadId":"msg_002","labelIds":["INBOX","UNREAD"],
         "snippet":"I cannot believe how buggy this software is...",
         "internalDate":"1740124200000",
         "payload":{"headers":[
             {"name":"Subject","value":"Complete waste of time - Cancel my account"},
             {"name":"From","value":"dissatisfied@corp.net"},
             {"name":"To","value":"support@techcompany.com"},
             {"name":"Date","value":"Fri, 21 Feb 2026 14:30:00 +0000"}]},
         "body_text_content":"I cannot believe how buggy this software is. I've lost 3 hours of work. Cancel my subscription NOW. I expect a confirmation within the hour."},
        {"id":"msg_003","threadId":"msg_003","labelIds":["INBOX"],
         "snippet":"Just following up on my previous email...",
         "internalDate":"1739606400000",
         "payload":{"headers":[
             {"name":"Subject","value":"Re: Partnership Proposal"},
             {"name":"From","value":"partner@business.com"},
             {"name":"To","value":"sales@techcompany.com"},
             {"name":"Date","value":"Sun, 15 Feb 2026 10:00:00 +0000"}]},
         "body_text_content":"Hi Sarah,\n\nJust following up on my previous email from last week. Have you had a chance to review the proposal?\n\n> On Mon, Feb 10, 2026 at 9:00 AM, Sarah wrote:\n> > Thanks, we will review it.\n"},
        {"id":"msg_004","threadId":"msg_004","labelIds":["INBOX","UNREAD"],
         "snippet":"I haven't heard back regarding the login issue...",
         "internalDate":"1739177100000",
         "payload":{"headers":[
             {"name":"Subject","value":"Checking in on ticket #5544"},
             {"name":"From","value":"john.doe@users.com"},
             {"name":"To","value":"support@techcompany.com"},
             {"name":"Date","value":"Mon, 10 Feb 2026 08:45:00 +0000"}]},
         "body_text_content":"Hello,\n\nI haven't heard back regarding the login issue I reported. Is there any update? It's been 5 days.\n\nBest,\nJohn"},
        {"id":"msg_005","threadId":"msg_005","labelIds":["INBOX"],
         "snippet":"I really like the new design!...",
         "internalDate":"1740220800000",
         "payload":{"headers":[
             {"name":"Subject","value":"Feedback on the new dashboard prototype"},
             {"name":"From","value":"beta.tester@innovate.io"},
             {"name":"To","value":"product@techcompany.com"},
             {"name":"Date","value":"Sat, 22 Feb 2026 11:20:00 +0000"}]},
         "body_text_content":"Hey team,\n\nI really like the new design! However, it would be great if we could export the charts to CSV. Is that something you can add to the roadmap?\n\nCheers,"},
        {"id":"msg_006","threadId":"msg_006","labelIds":["INBOX"],
         "snippet":"I love the app but my eyes hurt at night...",
         "internalDate":"1740009600000",
         "payload":{"headers":[
             {"name":"Subject","value":"Idea: Dark Mode"},
             {"name":"From","value":"night.owl@creative.com"},
             {"name":"To","value":"feedback@techcompany.com"},
             {"name":"Date","value":"Wed, 19 Feb 2026 23:00:00 +0000"}]},
         "body_text_content":"I love the app but my eyes hurt at night. Please add a dark mode option!\n\nSent from my iPhone"},
        {"id":"msg_007","threadId":"msg_007","labelIds":["INBOX","UNREAD"],
         "snippet":"Steps to reproduce: 1. Go to settings...",
         "internalDate":"1740232800000",
         "payload":{"headers":[
             {"name":"Subject","value":"Bug: 500 Error when uploading avatar"},
             {"name":"From","value":"qa.external@testing.com"},
             {"name":"To","value":"bugs@techcompany.com"},
             {"name":"Date","value":"Sat, 22 Feb 2026 15:00:00 +0000"}]},
         "body_text_content":"Steps to reproduce:\n1. Go to settings\n2. Click upload avatar\n3. Select image.png\n4. Error 500 appears.\n\nPlease fix this as we cannot update our profiles."},
        {"id":"msg_008","threadId":"msg_008","labelIds":["INBOX","UNREAD"],
         "snippet":"The app crashes immediately after the splash screen...",
         "internalDate":"1740069900000",
         "payload":{"headers":[
             {"name":"Subject","value":"Crash on startup (Windows 11)"},
             {"name":"From","value":"win.user@legacy.com"},
             {"name":"To","value":"support@techcompany.com"},
             {"name":"Date","value":"Thu, 20 Feb 2026 16:45:00 +0000"}]},
         "body_text_content":"The app crashes immediately after the splash screen on my Windows 11 machine.\n\n[LOG CONTENT REDACTED]"},
        {"id":"msg_009","threadId":"msg_009","labelIds":["INBOX"],
         "snippet":"We are interested in the enterprise plan...",
         "internalDate":"1739875800000",
         "payload":{"headers":[
             {"name":"Subject","value":"Question about Enterprise pricing"},
             {"name":"From","value":"cto@bigcorp.com"},
             {"name":"To","value":"sales@techcompany.com"},
             {"name":"Date","value":"Tue, 18 Feb 2026 09:30:00 +0000"}]},
         "body_text_content":"Hi,\n\nWe are interested in the enterprise plan. Do you offer volume discounts for 50+ seats?\n\nThanks,"},
        {"id":"msg_010","threadId":"msg_010","labelIds":["INBOX"],
         "snippet":"We would like to invite you to speak...",
         "internalDate":"1737806400000",
         "payload":{"headers":[
             {"name":"Subject","value":"Invitation: Tech Summit 2026"},
             {"name":"From","value":"organizer@techsummit.com"},
             {"name":"To","value":"info@techcompany.com"},
             {"name":"Date","value":"Sat, 25 Jan 2026 12:00:00 +0000"}]},
         "body_text_content":"Dear Team,\n\nWe would like to invite you to speak at the upcoming Tech Summit.\n\nRegister here: https://techsummit.com/register"},
    ]