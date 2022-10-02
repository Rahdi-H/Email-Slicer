def main():
    print('Email splicer')
    email_input = input('enter your email: ')
    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split('.')
    print('User name is: ', username)
    print('domain is: ', domain)
    print('extensin is: ', extension)


main()