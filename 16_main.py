s = "38006F45291200"
#s = "D2FE28"
s = "EE00D40C823060"
s = "8A004A801A8002F478"
s = "620080001611562C8802118E34"
s = "C0015000016115A2E0802F182340"
s = "A0016C880162017C3686B18A3D4780"
s = "420D598021E0084A07C98EC91DCAE0B880287912A925799429825980593D7DCD400820329480BF21003CC0086028910097520230C80813401D8CC00F601881805705003CC00E200E98400F50031801D160048E5AFEFD5E5C02B93F2F4C11CADBBB799CB294C5FDB8E12C40139B7C98AFA8B2600DCBAF4D3A4C27CB54EA6F5390B1004B93E2F40097CA2ECF70C1001F296EF9A647F5BFC48C012C0090E675DF644A675DF645A7E6FE600BE004872B1B4AAB5273ED601D2CD240145F802F2CFD31EFBD4D64DD802738333992F9FFE69CAF088C010E0040A5CC65CD25774830A80372F9D78FA4F56CB6CDDC148034E9B8D2F189FD002AF3918AECD23100953600900021D1863142400043214C668CB31F073005A6E467600BCB1F4B1D2805930092F99C69C6292409CE6C4A4F530F100365E8CC600ACCDB75F8A50025F2361C9D248EF25B662014870035600042A1DC77890200D41086B0FE4E918D82CC015C00DCC0010F8FF112358002150DE194529E9F7B9EE064C015B005C401B8470F60C080371460CC469BA7091802F39BE6252858720AC2098B596D40208A53CBF3594092FF7B41B3004A5DB25C864A37EF82C401C9BCFE94B7EBE2D961892E0C1006A32C4160094CDF53E1E4CDF53E1D8005FD3B8B7642D3B4EB9C4D819194C0159F1ED00526B38ACF6D73915F3005EC0179C359E129EFDEFEEF1950005988E001C9C799ABCE39588BB2DA86EB9ACA22840191C8DFBE1DC005EE55167EFF89510010B322925A7F85A40194680252885238D7374C457A6830C012965AE00D4C40188B306E3580021319239C2298C4ED288A1802B1AF001A298FD53E63F54B7004A68B25A94BEBAAA00276980330CE0942620042E3944289A600DC388351BDC00C9DCDCFC8050E00043E2AC788EE200EC2088919C0010A82F0922710040F289B28E524632AE0"


conv = {}
conv["0"] = "0000"
conv["1"] = "0001"
conv["2"] = "0010"
conv["3"] = "0011"
conv["4"] = "0100"
conv["5"] = "0101"
conv["6"] = "0110"
conv["7"] = "0111"
conv["8"] = "1000"
conv["9"] = "1001"
conv["A"] = "1010"
conv["B"] = "1011"
conv["C"] = "1100"
conv["D"] = "1101"
conv["E"] = "1110"
conv["F"] = "1111"

b = ""
for x in s:
    b += conv[x]

def parsePacket(b, i):
    c = 0
    version = b[i:i+3]
    c += int(version, 2)
    type_id = b[i+3:i+6]
    print(type_id)
    if type_id == "100":
        print("Literal value")
        l = ""
        j = i + 6
        continuer = True
        while continuer:
            continuer = (b[j] == "1")
            l += b[j+1:j+5]
            j += 5
        return (j, c, int(l, 2))
    else:
        print("Operator")
        length_type = b[i+6]

        values = []


        if length_type == "0":
            length = int(b[i+7:i+22], 2)
            print(length)
            j = i+22
            while j < i + 22 + length:
                x = parsePacket(b, j)
                print(x)
                j = x[0]
                c += x[1]
                values.append(x[2])
            print(j, i + 22 + length)
        else:
            n = int(b[i+7:i+18], 2)
            print(n)
            j = i + 18
            for _ in range(n):
                x = parsePacket(b, j)
                print(x)
                j = x[0]
                c += x[1]
                values.append(x[2])

        if type_id == "000":
            value = sum(values)
        elif type_id == "001":
            # Product
            value = 1
            for x in values:
                value *= x
        elif type_id == "010":
            value = min(values)
        elif type_id == "011":
            value = max(values)
        elif type_id == "101":
            if values[0] > values[1]:
                value = 1
            else:
                value = 0
        elif type_id == "110":
            if values[0] < values[1]:
                value = 1
            else:
                value = 0
        elif type_id == "111":
            if values[0] == values[1]:
                value = 1
            else:
                value = 0
        return (j, c, value)

print(parsePacket(b, 0))
