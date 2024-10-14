import random
welcome_message = "welcome to CUPY GAMES!"
cupy_position = random.randint(1, 4)
print("*******************************")
print("f** {welcome_message} **")
print("*******************************")

nama_user = input(" masukan nama kamu: ")

print(f'''
Hallo {nama_user} ! coba perhatikan goa dibawa ini
|_| |_| |_| |_|
''')

pilihan_user= int(input("menurut kamu di goa berapa CUPY berada ? [1 / 2 / 3 / 4 /]: "))

if pilihan_user == cupy_position: 
    print(f"selamat {nama_user} kamu menang ! posisi CUPY ada goa {cupy_position} dan pilihan mu adalah goa nomor {pilihan_user} ")
else:
    print(f"kamu kala! posisi CUPY bukan berada  disitu tapi ada goa {cupy_position} sedangkan kamu memilih goa nomor {pilihan_user} ")