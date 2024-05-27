# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2024.

import sys, csv, re

codes = [{"code":"28588","system":"gprdproduct"},{"code":"24800","system":"gprdproduct"},{"code":"14930","system":"gprdproduct"},{"code":"14340","system":"gprdproduct"},{"code":"26098","system":"gprdproduct"},{"code":"14339","system":"gprdproduct"},{"code":"9503","system":"gprdproduct"},{"code":"28183","system":"gprdproduct"},{"code":"23231","system":"gprdproduct"},{"code":"14933","system":"gprdproduct"},{"code":"17712","system":"gprdproduct"},{"code":"20995","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('insulin-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["insulin-wockhar---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["insulin-wockhar---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["insulin-wockhar---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
