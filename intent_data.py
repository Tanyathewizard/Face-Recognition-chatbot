
# # This dictionary maps user intents (topics) to keywords and response templates
data = {
        "greet": {
        "keywords": [
            "hi", "hello", "hey", "good morning", "good afternoon",
            "good evening", "yo", "heyy", "what's up", "namaste",
             "morning", "sup", "hii", "heya","wassup"
        ],
        "responses": [
            "Hi there! How can I help you today?",
            "Hey! What would you like to know?",
            "Hello! Need something?",
            "Hi! Ask me anything."
        ]
    },
    "salary": {
        "keywords": [
            "salary", "payslip", "pay", "credited", "income", "payment",
            "salary date", "got salary", "download payslip",
            "salary not received", "check my pay", "when will I get paid",
            "salary slip", "money", "account credited", "where's my salary"
        ],
        "responses": [
            "Your salary should be credited by the end of the month.",
            "Payslips are available on the HR portal.",
            "Please check your bank aacount— it might already be there.",
            "If there's a delay, HR will send a notice."
        ]
    },

    "leave": {
        "keywords": [
            "leave", "apply leave", "vacation", "off", "holiday request",
            "leave balance", "remaining leaves", "how many leaves left",
            "request time off", "sick leave", "how to apply leave",
            "casual leave", "paid leave", "can I take leave", "leave portal"
        ],
        "responses": [
            "You can request leave through the system easily.",
            "Check your remaining leaves in your profile section.",
            "Just go to the leave tab and apply there.",
            "Talk to your manager if it's urgent leave."
        ]
    },

    "timing": {
        "keywords": [
            "timing", "office timing", "shift", "working hours",
            "start time", "end time", "what time office starts",
            "closing time", "log in time", "log out time",
            "when to come", "when do we leave", "working hours today", "what are the timings"
        ],
        "responses": [
            "Office is open from 9 AM to 6 PM.",
            "Try to be in by 9 — that's the start time.",
            "We usually log out by 6.",
            "Standard hours are 9 to 6 unless told otherwise."
        ]
    },

    "holiday": {
        "keywords": [
            "holiday", "holidays", "holiday list", "holiday calendar",
            "company holidays", "office closed", "off days", "next holiday",
            "weekend off", "upcoming holiday", "when is the holiday",
            "day off", "any leave on friday", "holiday coming up", "public holiday"
        ],
        "responses": [
           "Just log in to the portal and go to the holiday section — it’s all there."
            "There’s a public holiday coming up soon.",
            "No holidays this week as per the calendar.",
            "You can check the next off day on the portal."
            "The all holiday list are present on the portal"
        ]
    },
        "wfh": {
        "keywords": [
            "wfh", "work from home", "can i work from home", "remote work",
            "working remotely", "do we have wfh", "wfh allowed", "today wfh",
            "is wfh option available", "can i take wfh"
        ],
        "responses": [
            "WFH depends on your team and manager — it’s best to check with them first.",
            "If your role allows, you can request WFH through the portal or message your lead.",
            "Some teams allow WFH on certain days — check the policy or ask your manager.",
            "Usually, you need approval from your reporting manager for WFH."
        ]
    },
    "designation": {
    "keywords": [
        "designation", "my role", "job title", "position", 
        "what is my title", "current role", "job position"
    ],
    "responses": [
        "It's in your profile section.",
        "Check your dashboard — it's listed there.",
        "Your title shows on the portal top section.",
        "You'll find it under 'My Details'."
    ]
},

"promotion": {
    "keywords": [
        "promotion", "promoted", "next level", "designation change",
        "new role", "career growth", "position upgrade", 
        "when will I be promoted", "higher role", "growth opportunity"
    ],
    "responses": [
        "It’s discussed during reviews.",
        "Your manager will update you.",
        "Depends on performance and timing.",
        "You’ll be informed if eligible."
    ]
},

"resignation": {
    "keywords": [
        "resign", "resignation", "leave company", "quit job",
        "how to resign", "submit resignation", "exit process", 
        "I want to quit", "leaving the job","I want to quit my job"
    ],
    "responses": [
        "Use the 'Exit' option in the portal.",
        "Talk to your manager before starting the process.",
        "HR will guide you after you apply.",
        "Submit it through your profile section."
    ]
}
,     
       # EXIT CHAT INTENT
    "exit": {
        "keywords": [
            "exit", "quit", "bye", "goodbye", "see you", "i'm done","done now",
            "thanks that's all", "talk later", "i’m good now", "leave now",
            "done for today", "okay bye", "close chat", "end this","bie","see you later"
        ],
        "responses": [
            "Thank you !"
        ]
    },
          # UNKNOWN INTENT — fallback if no keyword matched
  
 "unknown": {
    "keywords": [],
    "responses": [
        "Apologies, I couldn't understand that.",
        "Could you please rephrase your question?",
        "Sorry, that wasn’t clear. Could you try again?",
        "I didn’t get that. Can you explain it another way?"
    ]
}

}
