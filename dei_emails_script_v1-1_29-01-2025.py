# a script to automate sending stupid emails to the government
# primarily in order to clog up their snitch email.
# This idea here is to fill the DEIAtruth@opm.gov snitch hotline with bogus emails so that they are
# less effective in reaching and acting on any potential "real" emails.
#
# v1.1 January 29th 2025
# It's a little sloppy, but it works.

# global variables you should change
email_logins = {"emailusername@gmail.com": "app password",
                "emailusername@gmail.com": "app password",
                }
send_limit = 150
send_randomized = False


# Global variables you don't have to change
import time
import smtplib
import random
import datetime
from email.utils import formataddr
from email.message import EmailMessage

smtp_server = "smtp.gmail.com"
smtp_port = 587
to_email = ["DEIAtruth@opm.gov", "amanda.scales@opm.gov", "DEIAreports@opm.gov"]

# Personalization vaiables
pre_random_dict = {"Doland I. Trumpf": ["78", "Washington, D.C.", "Un-President of the United States"],
                   "Melon Q. Husk": ["53", "Washington, D.C.", "Cabinet of the President", ],
                   "Jobert E. Blennedy, Jr.": ["71", "Washington, D.C", "Cabinet of the President"],
                   "Petey Hedgeseth": ["44", "Washington, D.C.", "Cabinet of the President"],
                   "Lindas McMcMahon": ["76", "Washington, D.C.", "Cabinet of the President"],
                   "DJ Dance": ["40 years", "Washington, D.C.", "Cabinet of the President"],
                   "Stefen Griller": ["39", "Washington, D.C.", "Pocket of the President"]}

first_names_list = ["Donald", "Elon", "JD", "John", "Jane", "Elizabeth", "Bruce", "Pete", "Dick", "Richard", "Maria",
                    "James",
                    "Liam", "Noah", "Oliver", "Mary", "Patricia", "Jennifer", "Linda", "Barbara", "Angela", "Jill",
                    "Robert",
                    "Chris", "Leon", "Mitch", "Karen", "Gary", "Jeremy", "Robert", "Mark", "Terence", "Denise",
                    "Ingrid",
                    "Dorothy", "Benjamine", "Matthew", "Walter", "Marco", "Scott", "Pete", "Pam", "Doug", "Brooke",
                    "Howard",
                    "Lori", "Linda", "Scott", "Sean", "Chris", "Kristi", "Amanda", "Charles", "Neil"]

last_names_list = ["Vega", "McDonovan", "Rebaba", "Sunderland", "Valentine", "Kennedy", "Redfield", "Musk", "Trump",
                   "Vance",
                   "Gunnarsson", "Rubio", "Besent", "Hegseth", "Bondi", "Burgum", "Smith", "Rollins", "Lutnick",
                   "Gates",
                   "Zuckerberg", "Turner", "Duffy", "Wright", "McMahon", "Collins", "Noem", "Johnson", "Williams",
                   "Brown",
                   "Jones", "Garcia", "Miller", "Davis", "Scales", "Ezell", "Gaiman", "Doe"]

signee_names = ["John", "Jane", "Elizabeth", "Bruce", "Pete", "Dick", "Richard", "Maria", "James",
                "Liam", "Noah", "Oliver", "Mary", "Patricia", "Jennifer", "Linda", "Barbara", "Angela", "Jill",
                "Chris", "Mitch", "Karen", "Gary", "Jeremy", "Mark", "Terence", "Denise",
                "Dorothy", "Matthew", "Walter", "Scott", "Pete", "Pam", "Doug", "Brooke", "Howard",
                "Lori", "Linda", "Scott", "Sean", "Chris", "Amanda", "Charles", ]

age = list(range(35, 78))

workplace = ["Chicago, IL", "New York, NY", "Los Angeles, CA", "Houston, TX", "Phoenix, AZ", "Philadelphia, PA",
             "Washington, DC",
             "San Antonio, TX", "Columbus, OH", "Denver, CO", "Indianapolis, IN", "Oklahoma City, OK", "Nashville, TN",
             "Springfield, MO",
             "Boston, MA"]

department = ["National Credit Union Administration", "Department of Defense", "Federal Deposit Insurance Corporation",
              "Federal Trade Commission",
              "Office of Personnel Management", "Securities and Exchange Commission", "Internal Revenue Service",
              "Central Intelligence Agency", "Federal Bureau of Investigations", "Immigration and Customs Enforcement",
              "Secret Service", "Department of Homeland Security", "State Department", "Federal Reserve Board", ]

subject_opener = ["Potential DEI Hire: ", "DEI Description Change: ", "Catching DEI Report: ", "OPM DEI: ",
                  "DEI Executive Orders: ", "Got someone for DEI: ", "Position Change DEI: ", "Fire them for DEI: ",
                  "DEI Ideologies: ",
                  "Truth about DEI: ", "Time to go DEI: ", "Get them out of here DEI: ", "This is ridiculous DEI: ",
                  "Trying DEI on for size: ", "Report: ", "New Report: ", "That report your asked for: ",
                  "Some information: ",]


# Defining the message body and getting randomization involved
def message_build(first_name_set, last_name_set, age_set, workplace_set, department_set,
                  signee_fname_set, subj_set, recipient_email):
    msg = EmailMessage()

    if type(first_name_set) is list:
        first_name = random.choice(first_name_set)
        last_name = f" {random.choice(last_name_set)}"
        age_m = random.choice(age_set)
        city = random.choice(workplace_set)
        department_m = random.choice(department_set)
        signee_first = random.choice(signee_fname_set)
        signee_last = str(random.choice(last_name_set))[0]

        subject_m = random.choice(subj_set)
        subject_full = f"{subject_m}{first_name} {last_name}"

        sender = f"{signee_first} {signee_last}"

    else:
        first_name = first_name_set
        last_name = last_name_set
        age_m = age_set
        city = workplace_set
        department_m = department_set
        signee_first = signee_fname_set
        signee_last = signee_fname_set[0]

        subject_full = f"{subj_set}{first_name} {last_name}"

        sender = f"{signee_first} {signee_last}"

    msg["From"] = formataddr((f"{sender}", f"dummymail@gmail.com"))
    msg["To"] = formataddr((f"{recipient_email}", f"{recipient_email}"))
    msg["Subject"] = f"{subject_full}"

    message_body_text = (f"To whom it may concern,\n\n" +
                         f"According to sources and information available to me, it is my belief that I know of an individual " +
                         "who would fit the description of a DEI hire. As a matter of fact, I know many such people, and have been waiting " +
                         "eagerly to turn these people in to the proper authorities. Hence, why you may see many emails " +
                         "with my name. Per the January 21st 2025 memorandum RE: Initial Guidance Regarding " +
                         "DEIA Executive Orders, it is my duty to report on anyone who represents a disgraceful DEI holdover. Therefore, " +
                         "I have reason to believe that the following person is a DEI hire and/or is associated with DEI initiatives. " +
                         "Furthermore, I believe that they have altered their work description and disguised themselves with imprecise language. " +
                         "It would be in the best interest of the Office of Personnel Management to investigate this individual quickly. " +
                         "\n\nI believe that they are a DEI hire because it is clear they have been hired due to their race, ethnicity, "
                         "sex, class, or religion, and do not possess the competence " +
                         "or ability to carry out their position to the extent expected of the U.S. Government. They are taking a " +
                         "federal job that should rightfully belong to a more qualified American, and they are disgracing the U.S. Government " +
                         "by introducing the woke agenda into our federal services. I believe this individual is as follows: \n\n" +
                         f"You should investigate {first_name}{last_name}, who is {age_m} years old. They currently reside in " +
                         f"{city} and are working for the the government office of the {department_m}.\n\n" +
                         "As an American citizen, it is my hope that you take this message with all seriousness and investigate my claims " +
                         "thoroughly. We have a chance to make a stronger country, free of the woke left and their racist DEI iniatives.\n\n" +
                         "God Bless America,\n" +
                         f"{signee_first} {signee_last}.\n")

    msg.set_content(message_body_text)

    return msg


# Running on an iterable dictionary of multiple emails
for username, password in email_logins.items():
    print(f"Sending emails from {username} email now...")
    processStartTime = datetime.datetime.now()

    email_count = 0
    random_count = 0
    from_email = username
    email_username = username
    app_password = password


    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(email_username, app_password)

        if send_randomized is True:
            send_limit_total = send_limit
            random_limit = len(pre_random_dict)

        elif send_randomized is False:
            if send_limit <= len(pre_random_dict):
                random_limit = send_limit
            else:
                random_limit = (send_limit - (send_limit % len(pre_random_dict)))
            send_limit_total = random_limit

        while email_count < send_limit_total:
            while random_count < random_limit:

                random_list_value = random_count % len(pre_random_dict)

                first = list(pre_random_dict.keys())[random_list_value]
                last = ""
                age_pr = list(pre_random_dict.values())[random_list_value][0]
                city_pr = list(pre_random_dict.values())[random_list_value][1]
                department_pr = list(pre_random_dict.values())[random_list_value][2]
                signee_first = random.choice(first_names_list)
                signee_last = str(random.choice(last_names_list))
                subject_pr = str(random.choice(subject_opener))

                for i in to_email:
                    time.sleep(0.1)
                    send_message_target = message_build(first, last, age_pr, city_pr, department_pr, signee_first,
                                                        subject_pr, i)

                    smtp.send_message(send_message_target)

                print("Targeted emails sent!")
                random_count += 1
                email_count += 1

            while email_count < send_limit_total:
                for i in to_email:
                    time.sleep(0.1)
                    send_message_random = message_build(first_names_list, last_names_list, age, workplace, department,
                                                        signee_names,
                                                        subject_opener, i)

                    smtp.send_message(send_message_random)

                print("Randomized emails sent!")
                email_count += 1

    processEndTime = datetime.datetime.now()
    print(f"\nYou just sent {email_count} unique emails to {len(to_email)} email addresses, for a total of "
          f"{str(int(email_count) * len(to_email))} emails!\n"
          f"This took your computer {str(processEndTime - processStartTime)} to complete.\n"
          f"By helping to clog the gears of fascist bureaucracy with meaningless nonsense,\n"
          f"you have committed civil disobience in search of a better world. Excellent work.\n"
          f"Consider joining the U.S. General Strike: https://generalstrikeus.com/ \n"
          f"or the Party for Socialism and Liberation: https://pslweb.org/ \n"
          f"or a similar political movement to continue your actions. \n"
          f"Remember, if a cop asks you something: you don't know anything.\n")

print("All listed email addresses used for civil disobedience. Have a nice day.")


# Changelog:
# v1.0 initial release with basic abilities
# v1.1 added iterable dictionary option so you can have this perform the same function over
# several emails per script run.
#
# Please note there is a 500-email daily limit on gmail.
#
# The only variables you need to change are the "email_username", "app_password", "send_limit", and send_randomized.
# email_username: the username/email address of the sending email.
# app_password: the password used to log into the sending email. regular password usually doesn't work.
# send_limit: how many emails get sent. If send_randomized is False, rounds down to the
# nearest whole number divisible by the number of pre-selected names.
# send_randomized: A true/false option to turn on a mode that randomizes "target" information to
# be a combination of common first and last names, with
# randomized locations, ages, and federal departments.
#
# This script offers two scenarios: targeted emails, with "real" people (i.e. Doland Trumpf, Melon Husk), and
# randomized emails, which generates a bogus email with fake names, ages, and locations as a red herring.
# The randomized emails are not intended to be real people, but fakes names, like "John Doe" to further
# clog the system of fascist bureaucracy. It might be better to leave this mode as "false," unless
# you feel like really throwing as many names at the wall as possible.
#
# it requires a valid email address, but if you're using gmail, you can't log in with your regular password.
# you have to set up an app password, which requires 2fa, which requires a phone number,
# but you can get around this by using the google authenticator app instead. Once you generate
# an app passowrd, use that instead.
#
# The first emails sent are always real names of whoever is in the pre_random_list
# Feel free to customize the individual aspects of this list, or the names in the randomized list below that.
#
# Not comfortable sending a misleading gibberish witch hunt email with randomized personal information
# that could, in theory, be a real person?
# Change "send_randomized" to "False" to turn this feature off! Now it just sends targeted emails
# against specific people in power, from the "pre_random_dict" list. The script will iterate
# through the list of pre-selected names until it reaches your send limit.



'''
# Backup code lines:
# smtp.sendmail(from_email, i, body_text_pr)
'''
