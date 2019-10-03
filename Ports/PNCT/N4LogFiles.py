filename = 'C:\\Users\\seangi\\OneDrive - Ports America\\_Projects\\EDW\\N4\\PNCT\\20171106Logs\\allfiles.txt'
results_file = 'C:\\Users\\seangi\\OneDrive - Ports America\\_Projects\\EDW\\N4\\PNCT\\20171106Logs\\results.txt'

containers = ['TCKU9507980','WFHU1177495','AMFU8756533','MEDU6920400','PONU1889644','MEDU8060272','MSCU9394684',
              'INKU6517076','MEDU7173612','FCIU4281457','BEAU4217141','MNBU3750466','SUDU7713358','MRKU2288060',
              'BMOU6908804','MEDU8678131','MEDU7501012','GLDU4096085','TCLU5869546']
with open(filename) as f:
    for line in f:
        for container in containers:
            if container in line:
                with open(results_file, 'a') as file_object:
                    file_object.write(line.rstrip() + '\n')

