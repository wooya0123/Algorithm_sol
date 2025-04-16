while True:
    password = input()
    vowels = ['a','e','i','o','u']
    res = 'acceptable'
    check1 = False

    if password == 'end':
        break
    else:
        last_word = None

        vowel_check = 0
        consonant_check = 0

        for word in password:
            # 중복 글자 방지
            if not last_word:
                last_word = word
            elif word == 'e' and last_word == 'e':
                pass
            elif word == 'o' and last_word == 'o':
                pass
            elif word != last_word:
                last_word = word
            elif word == last_word:
                res = 'not acceptable'
                break

            # 모음일 때
            if word in vowels:
                check1 = True

                # 모음 중복 출현 체크
                if consonant_check == 0:
                    vowel_check += 1
                else:
                    consonant_check = 0
                    vowel_check += 1

                if vowel_check >= 3:
                    res = 'not acceptable'
                    break

            # 자음일 때
            else:
                if vowel_check == 0:
                    consonant_check += 1
                else:
                    vowel_check = 0
                    consonant_check += 1

                if consonant_check >= 3:
                    res = 'not acceptable'
                    break
        else:
            if check1 == False:
                res = 'not acceptable'
    print(f'<{password}> is {res}.')