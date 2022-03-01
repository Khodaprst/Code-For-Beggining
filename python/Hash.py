from hashlib import sha256
import csv

def hash_password_hack(input_file_name , output_file_name):
    # khandan file input.
    with open(input_file_name) as fin:
        reader = csv.reader(fin)
        # motaghayer (hp) yek dict baraye hash haye range 1000 ta 9999 ast.
        # motaghayer (new_hp) yek dict baraye name va password hack shode ast.
        hp = {}
        new_hp = {}
        # in halghe hash haye range 1000 ta 9999 ra vared dict (hp) mikonad.
        for i in range(1000 , 9999):
            hash_jadid = sha256(str(i).encode())
            hash_jadid = hash_jadid.hexdigest()
            hp[hash_jadid] = i
        # halghe aval name va hash ra khat be khat az file input mikhanad.
        # halghe dovom check mikonad hash haye mojod dar file input ba hash haye dakhel dict (hp) motabeghat darad ya na. 
        # agar motabeghat dashtand password va name ra gerefte va dar dakhel dict (new_hp) migozarad
        for radif in reader:
            name = radif[0]
            hash_in_reader = radif[1]
            for hach_in_hp in hp.keys():
                if hash_in_reader == hach_in_hp:
                    new_hp[name]=hp.get(hach_in_hp)
    # dar code zir name ha va password hayii ke hack shodand ra vared yek file jadid mikonim
    with open(output_file_name , 'w') as out:
        count = 0
        for names in new_hp:
            count += 1
            if count == 1:
                out.write(names + ',' + str(new_hp.get(names)))
            else:
                out.write('\n' + names + ',' + str(new_hp.get(names)))

in_out_file_name = input()
print(hash_password_hack('input_file_name.csv','output_file_name.csv'))

