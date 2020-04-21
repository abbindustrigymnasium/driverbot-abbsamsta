import xml.etree.ElementTree as ET
import xlsxwriter

stationNames = ["Slussen", "Gamla stan", "T-Centralen", "Hötorget", "Rådmansgatan", "Odenplan", "S:t Eriksplan", "Fridhemsplan", "Thorildsplan", "Kristineberg", "Alvik", "Stora mossen", "Abrahamsberg", "Brommaplan", "Åkeshov", "Ängbyplan", "Islandstorget", "Blackeberg", "Råcksta", "Vällingby", "Johannelund", "Hässelby gård", "Hässelby strand", "Medborgarplatsen", "Skanstull", "Gullmarsplan", "Skärmarbrink", "Globen", "Enskede gård", "Sockenplan", "Svedmyra", "Stureby", "Bandhagen", "Högdalen", "Rågsved", "Hagsätra", "Blåsut", "Sandsborg", "Skogskyrkogården", "Tallkrogen", "Gubbängen", "Hökarängen", "Farsta", "Farsta strand", "Hammarbyhöjden", "Björkhagen", "Kärrtorp", "Bagarmossen", "Skarpnäck",
                "Östermalmstorg", "Karlaplan", "Gärdet", "Ropsten", "Stadion", "Tekniska högskolan", "Universitetet", "Bergshamra", "Danderyds sjukhus", "Mörby centrum", "Mariatorget", "Zinkensdamm", "Hornstull", "Liljeholmen", "Aspudden", "Örnsberg", "Axelsberg", "Mälarhöjden", "Bredäng", "Sätra", "Skärholmen", "Vårberg", "Vårby gård", "Masmo", "Fittja", "Alby", "Hallunda", "Norsborg", "Midsommarkransen", "Telefonplan", "Hägerstensåsen", "Västertorp", "Fruängen", "Kungsträdgården", "Rådhuset", "Stadshagen", "Västra skogen", "Solna centrum", "Näckrosen", "Hallonbergen", "Kymlinge norrut", "Kista", "Husby", "Akalla", "Huvudsta", "Solna strand", "Sundbybergs centrum", "Duvbo", "Rissne", "Rinkeby", "Tensta", "Hjulsta",
                ]
stationNumber = ["1011", "1021", "1051", "1111", "1121", "1131", "1141", "1151", "1161", "1171", "1201", "1211", "1221", "1231", "1241", "1251", "1261", "1271", "1281", "1301", "1311", "1321", "1331", "1511", "1521", "1551", "1601", "1611", "1621", "1631", "1641", "1651", "1661", "1701", "1711", "1721", "1811", "1821", "1831", "1841", "1851", "1861", "1871", "1881", "1911", "1921", "1931", "1941", "1951", "2101",
                 "2111", "2121", "2131", "2211", "2221", "2231", "2241", "2251", "2301", "2511", "2521", "2531", "2601", "2611", "2621", "2631", "2641", "2651", "2701", "2711", "2721", "2731", "2741", "2751", "2761", "2771", "2781", "2811", "2821", "2831", "2841", "2851", "3031", "3131", "3161", "3201", "3211", "3221", "3231", "3241", "3251", "3261", "3271", "3411", "3421", "3431", "3441", "3451", "3461", "3471", "3481"
                 ]


# Funktioner till funktinerna


def getStationName(x):
    try:
        x = stationNames[stationNumber.index(x[-4:])]
    except:
        x = ""
    return x


def getBracketInfo(x, info):
    a = info.split(x)
    a = a[1].split("/")
    a = (a[0].replace(">", "")).replace("<", "")
    return a

    # Kolumn-specifika funktioner


def CstLabel(x):
    x = getBracketInfo("CstLabel", x)
    x = x[-4:]
    return x


def CstLabels(x):
    x = x.split("CstLabels")
    x = (x[1].replace("</b:string>", "")).split("<b:string>")
    x.remove(x[0])
    y = ""
    for car in x:
        y += car.replace("</", "")[-4:] + " "
    return y


def VehicleModel(x):
    x = getBracketInfo("VehicleModel", x)
    return x


def CarTypes(x):
    x = x.split("CarTypes")
    x = (x[1].replace("</b:string>", "")).split("<b:string>")
    x.remove(x[0])
    y = ""
    for car in x:
        y += car.replace("</", "") + "  "
    return y


def BlockId(x):
    x = getBracketInfo("BlockId", x)
    return x


def DrivingDirection(x):
    x = getBracketInfo("DrivingDirection", x)
    return x


def CurrentStationID(x):
    x = getBracketInfo("CurrentStation", x)
    return x


def CurrentStation(x):
    x = getBracketInfo("CurrentStation", x)
    x = getStationName(x)
    return x


def NextStationID(x):
    x = x.replace("DistanceToNextStationM", "")
    x = getBracketInfo("NextStation", x)
    return x


def NextStation(x):
    x = x.replace("DistanceToNextStationM", "")
    x = getBracketInfo("NextStation", x)
    x = getStationName(x)
    return x


def DistanceToNextStationM(x):
    x = getBracketInfo("DistanceToNextStationM", x)
    return x


def DestinationStationID(x):
    x = getBracketInfo("DestinationStation", x)
    return x


def DestinationStation(x):
    x = getBracketInfo("DestinationStation", x)
    x = getStationName(x)
    return x


def DoorOpen(x):
    x = getBracketInfo("DoorOpen", x)
    return x


def DoorsClosed(x):
    x = getBracketInfo("DoorsClosed", x)
    return x


def HasChanged(x):
    x = getBracketInfo("HasChanged", x)
    return x


def LastUpdatedDate(x):
    x = getBracketInfo("LastUpdated", x)
    x = x.split("T")[0]
    return x


def LastUpdatedTime(x):
    x = getBracketInfo("LastUpdated", x)
    x = x.split("T")[1]
    return x


def MaxNumberOfStreams(x):
    x = getBracketInfo("MaxNumberOfStreams", x)
    return x


def RawPacket(x):
    a = x.split("<CstInfos>")
    b = a[1].split("</CstInfos>")
    d = b[0].replace("</CstInfo>", "")
    e = d.split("<CstInfo>")
    e.remove(e[0])
    f = []
    for info in e:
        f.append(info)
    return f


# while run:
print('1. Exportera wireshark filen som pdml.\tArkiv > Exportera packet dissekeringar > As PDML XML\n' +
      '2. Lägg filen och programmet i samma mapp.\n' +
      '3. Kör programmet så skapas xlsx filen i samma mapp.\n' +
      '\nProgrammet krachar om den inte hittar pdml filen' +
      '\nOm det redan finns en xlsx fil med samma namn så får den inte vara öppen. '
      )
fileName = input("Filename > ")

# xlsx file maker
workbook = xlsxwriter.Workbook(fileName + '.xlsx')

centrum_format = workbook.add_format({'align': 'center'})
false_format = workbook.add_format({'bg_color': '#f5c4c4'})
true_format = workbook.add_format({'bg_color': '#c1f5c1'})

wiresharkFile = fileName + ".pdml"
root = ET.parse(wiresharkFile).getroot()

CstLabelList = []
columns = []

for packet in root:
    CstInfo = []
    packetNumber = packet[0][0].attrib['show']
    packetArrival = packet[0][3].attrib['show']

    for proto in packet:
        for field in proto:
            if field.attrib['name'] == "http.file_data":
                for infos in RawPacket(field.attrib['show']):
                    if CstLabel(infos) not in CstLabelList:
                        CstLabelList.append(CstLabel(infos))
                        columns.append([])

                    for listIndex, listItem in enumerate(CstLabelList, start=0):

                        if CstLabel(infos) == listItem:
                            columns[listIndex].append([
                                packetNumber,
                                packetArrival.strip("Västeuropa, normaltid"),
                                CstLabel(infos),
                                CstLabels(infos),
                                VehicleModel(infos),
                                CarTypes(infos),
                                BlockId(infos),
                                DrivingDirection(infos),
                                CurrentStationID(infos),
                                CurrentStation(infos),
                                NextStationID(infos),
                                NextStation(infos),
                                DistanceToNextStationM(infos),
                                DestinationStationID(infos),
                                DestinationStation(infos),
                                DoorOpen(infos),
                                DoorsClosed(infos),
                                HasChanged(infos),
                                LastUpdatedDate(infos),
                                LastUpdatedTime(infos),
                                MaxNumberOfStreams(infos)
                            ])


for sheetIndex, sheet in enumerate(columns, start=0):
    try:
        worksheet = workbook.add_worksheet(sheet[1][2])
        titel_format = workbook.add_format(
            {'bg_color': '#d9d9d9', 'border': 1, 'text_wrap': 'true', 'bold': 'true'})

        worksheet.set_column('A:V', None, centrum_format)

        worksheet.write('A1', 'Frame Number', titel_format)
        worksheet.set_column('A:A', 55/7)
        worksheet.write('B1', 'Frame Arrival', titel_format)
        worksheet.set_column('B:B', 200/7)
        worksheet.write('C1', 'CstLabel', titel_format)
        worksheet.set_column('C:C', 60/7)
        worksheet.write('D1', 'CstLabels', titel_format)
        worksheet.set_column('D:D', 75/7)
        worksheet.write('E1', 'Vehicle Model', titel_format)
        worksheet.set_column('E:E', 50/7)
        worksheet.write('F1', 'CarTypes', titel_format)
        worksheet.set_column('F:F', 180/7)
        worksheet.write('G1', 'BlockId', titel_format)
        worksheet.set_column('G:G', 80/7)
        worksheet.write('H1', 'Driving Direction', titel_format)
        worksheet.set_column('H:H', 65/7)
        worksheet.write('I1', 'Current StationID', titel_format)
        worksheet.set_column('I:I', 80/7)
        worksheet.write('J1', 'Current Station', titel_format)
        worksheet.set_column('J:J', 105/7)
        worksheet.write('K1', 'Next StationID', titel_format)
        worksheet.set_column('K:K', 80/7)
        worksheet.write('L1', 'Next Station', titel_format)
        worksheet.set_column('L:L', 105/7)
        worksheet.write('M1', 'Distance To Next StationM', titel_format)
        worksheet.set_column('M:M', 70/7)
        worksheet.write('N1', 'Destination StationID', titel_format)
        worksheet.set_column('N:N', 80/7)
        worksheet.write('O1', 'Destination Station', titel_format)
        worksheet.set_column('O:O', 105/7)
        worksheet.write('P1', 'Door Open', titel_format)
        worksheet.set_column('P:P', 40/7)
        worksheet.write('Q1', 'Doors Closed', titel_format)
        worksheet.set_column('Q:Q', 43/7)
        worksheet.write('R1', 'Has Changed', titel_format)
        worksheet.set_column('R:R', 56/7)
        worksheet.write('S1', 'Last Updated Date', titel_format)
        worksheet.set_column('S:S', 70/7)
        worksheet.write('T1', 'Last Updated Time', titel_format)
        worksheet.set_column('T:T', 120/7)
        worksheet.write('U1', 'Max Number Of Streams', titel_format)
        worksheet.set_column('U:U', 72/7)

        row = 1
        col = 0
        for rows in sheet:
            worksheet.write(row, col+0, rows[0])
            worksheet.write(row, col+1, rows[1])
            worksheet.write(row, col+2, rows[2])
            worksheet.write(row, col+3, rows[3])
            worksheet.write(row, col+4, rows[4])
            worksheet.write(row, col+5, rows[5])
            worksheet.write(row, col+6, rows[6])
            worksheet.write(row, col+7, rows[7])
            worksheet.write(row, col+8, rows[8])
            worksheet.write(row, col+9, rows[9])
            worksheet.write(row, col+10, rows[10])
            worksheet.write(row, col+11, rows[11])
            worksheet.write(row, col+12, rows[12])
            worksheet.write(row, col+13, rows[13])
            worksheet.write(row, col+14, rows[14])
            worksheet.write(row, col+15, rows[15])
            worksheet.write(row, col+16, rows[16])
            worksheet.write(row, col+17, rows[17])
            worksheet.write(row, col+18, rows[18])
            worksheet.write(row, col+19, rows[19])
            worksheet.write(row, col+20, rows[20])
            row += 1

        worksheet.conditional_format('P1:R10000', {'type':     'cell',
                                                   'criteria': '==',
                                                   'value':    '"false"',
                                                   'format':   false_format})

        worksheet.conditional_format('P1:R10000', {'type':   'cell',
                                                   'criteria': '==',
                                                   'value':    '"true"',
                                                   'format':   true_format})

        worksheet.freeze_panes(1, 0)

    except:
        pass

workbook.close()
