import pyodbc

def get_lines_with(input_str, substr):
    """
    Get all lines containing a substring.

    Args:
        input_str (str): String to get lines from.
        substr (str): Substring to look for in lines.

    Returns:
        list[str]: List of lines containing substr.
    """
    lines = []
    for line in input_str.strip().split('\n'):
        if substr.upper() in line:
            #lines.append(line)
            print(line)
            #return(line)
    #print(lines)


def txt_lines_with(fname, substr):
    """
    Get all lines in a .txt file containing a substring.

    Args:
        fname (str): File name to open.
        substr (str): Substring to look for in lines.

    Returns:
        list[str]: List of lines containing substr.
    """
    f_contents = open(fname, 'r').read()
    return get_lines_with(f_contents, substr)

#path = r'C:\Users\seangi\OneDrive - Ports America\_Projects\EDW\Claims\DocsAndNotes\4-20 Release DB Scripts\DB scripts\1-JDICM_Upgrade_From_2016.20_To_Latest.sql'
#path = r'C:\Users\seangi\OneDrive - Ports America\_Projects\EDW\Claims\DocsAndNotes\4-20 Release DB Scripts\DB scripts\2-JDICM_AllProcs.sql'
#path = r'C:\Users\seangi\OneDrive - Ports America\_Projects\EDW\Claims\DocsAndNotes\4-20 Release DB Scripts\DB scripts\3-JDICM_Maintenance.sql'
#path = r'C:\Users\seangi\OneDrive - Ports America\_Projects\EDW\Claims\DocsAndNotes\4-20 Release DB Scripts\DB scripts\4-Ports CM-6123 Incidents display as claims-24611.sql'
path = r'C:\Users\seangi\OneDrive - Ports America\_Projects\EDW\Claims\DocsAndNotes\4-20 Release DB Scripts\DB scripts\PythonTestFile.sql'


cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=CASC9MSDB03;"
                      "Database=stg_JDICMPortsAmerica_Prd;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()
cursor.execute('SELECT name FROM sys.tables')

for row in cursor:
    statement = "DROP TABLE " + str(row).strip("(),''")
    statement = statement[:-3]
    #print(statement)
    txt_lines_with(path, "DROP TABLE Claims")