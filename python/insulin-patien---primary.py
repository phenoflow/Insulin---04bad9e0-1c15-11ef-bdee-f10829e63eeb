# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2024.

import sys, csv, re

codes = [{"code":"28666","system":"gprdproduct"},{"code":"22946","system":"gprdproduct"},{"code":"19977","system":"gprdproduct"},{"code":"5267","system":"gprdproduct"},{"code":"58995","system":"gprdproduct"},{"code":"5789","system":"gprdproduct"},{"code":"6730","system":"gprdproduct"},{"code":"57153","system":"gprdproduct"},{"code":"59311","system":"gprdproduct"},{"code":"6378","system":"gprdproduct"},{"code":"58578","system":"gprdproduct"},{"code":"56656","system":"gprdproduct"},{"code":"59243","system":"gprdproduct"},{"code":"16959","system":"gprdproduct"},{"code":"47751","system":"gprdproduct"},{"code":"56624","system":"gprdproduct"},{"code":"6991","system":"gprdproduct"},{"code":"39150","system":"gprdproduct"},{"code":"7127","system":"gprdproduct"},{"code":"58754","system":"gprdproduct"},{"code":"11521","system":"gprdproduct"},{"code":"5769","system":"gprdproduct"},{"code":"57388","system":"gprdproduct"},{"code":"59133","system":"gprdproduct"},{"code":"17076","system":"gprdproduct"},{"code":"5967","system":"gprdproduct"},{"code":"6228","system":"gprdproduct"},{"code":"11878","system":"gprdproduct"},{"code":"30305","system":"gprdproduct"},{"code":"9702","system":"gprdproduct"},{"code":"5634","system":"gprdproduct"},{"code":"14646","system":"gprdproduct"},{"code":"57387","system":"gprdproduct"},{"code":"13009","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('insulin-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["insulin-patien---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["insulin-patien---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["insulin-patien---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
