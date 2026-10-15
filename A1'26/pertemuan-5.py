# Mulai
# while True:
# Masukkan Nilai A, B, dan C
# If A > B dan C, maka tampilkan "Nilai A adalah yang terbesar"
# elif B > A dan C, maka tampilkan "Nilai B adalah yang terbesar"
# elif C > A dan B, maka tampilkan "Nilai C adalah yang terbesar"
# if A = B dan C, maka tampilkan "Nilai A, B, dan C adalah sama"
# elif A = B, maka tampilkan "Nilai A dan B adalah sama"
# elif A = C, maka tampilkan "Nilai A dan C adalah sama"
# elif B = C, maka tampilkan "Nilai B dan C adalah sama"
# if A < B dan C, maka tampilkan "Nilai A adalah yang terkecil"
# elif B < A dan C, maka tampilkan "Nilai B adalah yang terkecil"
# elif C < A dan B, maka tampilkan "Nilai C adalah yang terkecil"
# if A = B dan A > C, maka tampilkan "Nilai A dan B adalah yang terbesar"
# elif A = C dan A > B, maka tampilkan "Nilai A dan C adalah yang terbesar"
# elif B = C dan B > A, maka tampilkan "Nilai B dan C adalah yang terbesar"
# end while
# Selesai

while True:
    A = int(input("Masukkan nilai A: "))
    B = int(input("Masukkan nilai B: "))
    C = int(input("Masukkan nilai C: "))
    if A > B and A > C:
        print("Nilai A adalah yang terbesar")
    elif B > A and B > C:
        print("Nilai B adalah yang terbesar")
    elif C > A and C > B:
        print("Nilai C adalah yang terbesar")
    
    if A == B and A == C:
        print("Nilai A, B, dan C adalah sama")
    elif A == B:
        print("Nilai A dan B adalah sama")
    elif A == C:
        print("Nilai A dan C adalah sama")
    elif B == C:
        print("Nilai B dan C adalah sama")

    if A < B and A < C:
        print("Nilai A adalah yang terkecil")
    elif B < A and B < C:
        print("Nilai B adalah yang terkecil")
    elif C < A and C < B:
        print("Nilai C adalah yang terkecil")

    if A == B and A > C:
        print("Nilai A dan B adalah yang terbesar")
    elif A == C and A > B:
        print("Nilai A dan C adalah yang terbesar")
    elif B == C and B > A:
        print("Nilai B dan C adalah yang terbesar")

    if A == B and A < C:
        print("Nilai A dan B adalah yang terkecil")
    elif A == C and A < B:
        print("Nilai A dan C adalah yang terkecil")
    elif B == C and B < A:
        print("Nilai B dan C adalah yang terkecil")
