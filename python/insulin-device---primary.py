# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2024.

import sys, csv, re

codes = [{"code":"53251","system":"gprdproduct"},{"code":"14362","system":"gprdproduct"},{"code":"7400","system":"gprdproduct"},{"code":"55687","system":"gprdproduct"},{"code":"56691","system":"gprdproduct"},{"code":"55603","system":"gprdproduct"},{"code":"19877","system":"gprdproduct"},{"code":"14330","system":"gprdproduct"},{"code":"52522","system":"gprdproduct"},{"code":"17336","system":"gprdproduct"},{"code":"41959","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('insulin-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["insulin-device---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["insulin-device---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["insulin-device---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
