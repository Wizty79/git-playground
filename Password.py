#secret = 'lonely'
#pw = ''

#while pw != secret:
#    pw = input("what's the secret word?!")


#or

secret = 'lonely'
pw = ''
auth = False
count = 0
max_attempt = 5

while pw != secret:
    count += 1
    if count > max_attempt: break #break will break all the way out of the loop and skip the else clause
    if count == 3: continue #continue will shortcircut the loop and go back up to the top/test? without finishing the body of the loop so we only get 4 tries 
    pw = input(f"{count}: What's the secret word?")
else:
    auth = True

print("Authorized" if auth else "Blocked ...")



