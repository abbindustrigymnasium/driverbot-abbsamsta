import xml.etree.ElementTree as ET
import xlsxwriter

stationNames = ["Slussen", "Gamla stan", "T-Centralen", "Hötorget", "Rådmansgatan", "Odenplan", "S:t Eriksplan", "Fridhemsplan", "Thorildsplan", "Kristineberg", "Alvik", "Stora mossen", "Abrahamsberg", "Brommaplan", "Åkeshov", "Ängbyplan", "Islandstorget", "Blackeberg", "Råcksta", "Vällingby", "Johannelund", "Hässelby gård", "Hässelby strand", "Medborgarplatsen", "Skanstull", "Gullmarsplan", "Skärmarbrink", "Globen", "Enskede gård", "Sockenplan", "Svedmyra", "Stureby", "Bandhagen", "Högdalen", "Rågsved", "Hagsätra", "Blåsut", "Sandsborg", "Skogskyrkogården", "Tallkrogen", "Gubbängen", "Hökarängen", "Farsta", "Farsta strand", "Hammarbyhöjden", "Björkhagen", "Kärrtorp", "Bagarmossen", "Skarpnäck",
                "Östermalmstorg", "Karlaplan", "Gärdet", "Ropsten", "Stadion", "Tekniska högskolan", "Universitetet", "Bergshamra", "Danderyds sjukhus", "Mörby centrum", "Mariatorget", "Zinkensdamm", "Hornstull", "Liljeholmen", "Aspudden", "Örnsberg", "Axelsberg", "Mälarhöjden", "Bredäng", "Sätra", "Skärholmen", "Vårberg", "Vårby gård", "Masmo", "Fittja", "Alby", "Hallunda", "Norsborg", "Midsommarkransen", "Telefonplan", "Hägerstensåsen", "Västertorp", "Fruängen", "Kungsträdgården", "Rådhuset", "Stadshagen", "Västra skogen", "Solna centrum", "Näckrosen", "Hallonbergen", "Kymlinge norrut", "Kista", "Husby", "Akalla", "Huvudsta", "Solna strand", "Sundbybergs centrum", "Duvbo", "Rissne", "Rinkeby", "Tensta", "Hjulsta",
                ]
stationNumber = ["1011", "1021", "1051", "1111", "1121", "1131", "1141", "1151", "1161", "1171", "1201", "1211", "1221", "1231", "1241", "1251", "1261", "1271", "1281", "1301", "1311", "1321", "1331", "1511", "1521", "1551", "1601", "1611", "1621", "1631", "1641", "1651", "1661", "1701", "1711", "1721", "1811", "1821", "1831", "1841", "1851", "1861", "1871", "1881", "1911", "1921", "1931", "1941", "1951", "2101",
                 "2111", "2121", "2131", "2211", "2221", "2231", "2241", "2251", "2301", "2511", "2521", "2531", "2601", "2611", "2621", "2631", "2641", "2651", "2701", "2711", "2721", "2731", "2741", "2751", "2761", "2771", "2781", "2811", "2821", "2831", "2841", "2851", "3031", "3131", "3161", "3201", "3211", "3221", "3231", "3241", "3251", "3261", "3271", "3411", "3421", "3431", "3441", "3451", "3461", "3471", "3481"
                 ]
colIndexs = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1",
             "J1", "K1", "L1", "M1", "N1", "O1", "P1", "Q1", "R1", "S1", "T1", ]
colNames = ['Frame Number', 'Frame Arrival', "CstLabel",  "CstLabels",  "VehicleModel",  "CarTypes", "BlockId", "DrivingDirection", "CurrentStationID", "CurrentStation",
            "NextStationID", "NextStation", "DistanceToNextStationM", "DestinationStationID", "DestinationStation", "DoorOpen", "DoorsClosed", "HasChanged", "LastUpdated", 'MaxNumberOfStreams', ]


def GetStationName(x):
    a = ""

    for index, station in enumerate(stationNumber, start=0):
        chars = []
        for char in x:
            chars.append(char)
        stationID = ""
        try:
            stationID = chars[-4] + chars[-3] + chars[-2] + chars[-1]
        except:
            pass
        if station == stationID:
            a = stationNames[index]
    return a


def CstLabelShort(x):
    chars = []
    for char in x:
        chars.append(char)
    a = chars[10] + chars[11] + chars[12] + chars[13]
    return a


def BlockId(x):
    a = x.split("BlockId")
    b = (a[1].replace(">", "")).replace("</", "")
    return b


def CarTypes(x):
    a = x.split("CarTypes")
    b = (a[1].replace("</b:string>", "")).split("<b:string>")
    b.remove(b[0])
    c = []
    for car in b:
        c.append(car.replace("</", ""))
    d = ""
    for sak in c:
        d = d + sak + "  "
    return d


def CstLabel(x):
    a = x.split("CstLabel")
    b = (a[1].replace(">", "")).replace("</", "")
    c = CstLabelShort(b)
    return c


def CstLabels(x):
    a = x.split("CstLabels")
    b = (a[1].replace("</b:string>", "")).split("<b:string>")
    b.remove(b[0])
    c = []
    for car in b:
        carFix = CstLabelShort(car)
        c.append(carFix.replace("</", ""))
    d = ""
    for sak in c:
        d = d + sak + "  "
    return d


def CurrentStation(x):
    a = x.split("CurrentStation")
    b = (a[1].replace(">", "")).replace("</", "")
    c = GetStationName(b)
    return c


def CurrentStationID(x):
    a = x.split("CurrentStation")
    b = (a[1].replace(">", "")).replace("</", "")
    return b


def DestinationStation(x):
    a = x.split("DestinationStation")
    b = (a[1].replace(">", "")).replace("</", "")
    c = GetStationName(b)
    return c


def DestinationStationID(x):
    a = x.split("DestinationStation")
    b = (a[1].replace(">", "")).replace("</", "")
    return b


def DistanceToNextStationM(x):
    a = x.split("DistanceToNextStationM")
    b = (a[1].replace(">", "")).replace("</", "")
    return b


def DoorOpen(x):
    a = x.split("DoorOpen")
    b = (a[1].replace(">", "")).replace("</", "")
    return b


def DoorsClosed(x):
    a = x.split("DoorsClosed")
    b = (a[1].replace(">", "")).replace("</", "")
    return b


def DrivingDirection(x):
    a = x.split("DrivingDirection")
    b = (a[1].replace(">", "")).replace("</", "")
    return b


def HasChanged(x):
    a = x.split("HasChanged")
    b = (a[1].replace(">", "")).replace("</", "")
    return b


def LastUpdated(x):
    a = x.split("LastUpdated")
    b = (a[1].replace(">", "")).replace("</", "")
    return b


def MaxNumberOfStreams(x):
    a = x.split("MaxNumberOfStreams")
    b = (a[1].replace(">", "")).replace("</", "")
    return b


def NextStation(x):
    a = x.replace("DistanceToNextStationM", "")
    b = a.split("NextStation")
    c = (b[1].replace(">", "")).replace("</", "")
    d = GetStationName(c)
    return d


def NextStationID(x):
    a = x.replace("DistanceToNextStationM", "")
    b = a.split("NextStation")
    c = (b[1].replace(">", "")).replace("</", "")
    return c


def VehicleModel(x):
    a = x.split("VehicleModel")
    b = (a[1].replace(">", "")).replace("</", "")
    return b


def RawPacket(x):
    a = x.split("<CstInfos>")
    b = a[1].split("</CstInfos>")
    c = b[0]
    d = c.replace("</CstInfo>", "")
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
worksheet = workbook.add_worksheet()
titel_format = workbook.add_format(
    {'bg_color': '#d9d9d9', 'border': 1, 'text_wrap': 'true'})


centrum_format = workbook.add_format({'align': 'center'})
worksheet.set_column('A:T', None, centrum_format)


worksheet.write('A1', 'Frame Number', titel_format)
worksheet.set_column('A:A', 60/7)
worksheet.write('B1', 'Frame Arrival', titel_format)
worksheet.set_column('B:B', 200/7)
worksheet.write('C1', 'CstLabel', titel_format)
worksheet.set_column('C:C', 75/7)
worksheet.write('D1', 'CstLabels', titel_format)
worksheet.set_column('D:D', 75/7)
worksheet.write('E1', 'Vehicle Model', titel_format)
worksheet.set_column('E:E', 50/7)
worksheet.write('F1', 'CarTypes', titel_format)
worksheet.set_column('F:F', 100/7)
worksheet.write('G1', 'BlockId', titel_format)
worksheet.set_column('G:G', 80/7)
worksheet.write('H1', 'Driving Direction', titel_format)
worksheet.set_column('H:H', 65/7)
worksheet.write('I1', 'Current StationID', titel_format)
worksheet.set_column('I:I', 80/7)
worksheet.write('J1', 'Current Station', titel_format)
worksheet.set_column('J:J', 100/7)
worksheet.write('K1', 'Next Station', titel_format)
worksheet.set_column('K:K', 100/7)
worksheet.write('L1', 'Next StationID', titel_format)
worksheet.set_column('L:L', 80/7)
worksheet.write('M1', 'Distance To Next StationM', titel_format)
worksheet.set_column('M:M', 70/7)
worksheet.write('N1', 'Destination Station', titel_format)
worksheet.set_column('N:N', 100/7)
worksheet.write('O1', 'Destination StationID', titel_format)
worksheet.set_column('O:O', 80/7)
worksheet.write('P1', 'Door Open', titel_format)
worksheet.set_column('P:P', 50/7)
worksheet.write('Q1', 'Doors Closed', titel_format)
worksheet.set_column('Q:Q', 50/7)
worksheet.write('R1', 'Has Changed', titel_format)
worksheet.set_column('R:R', 60/7)
worksheet.write('S1', 'Last Updated', titel_format)
worksheet.set_column('S:S', 200/7)
worksheet.write('T1', 'Max Number Of Streams', titel_format)
worksheet.set_column('T:T', 75/7)

wiresharkFile = fileName + ".pdml"
root = ET.parse(wiresharkFile).getroot()

row = 1
col = 0

for packet in root:
    CstInfo = []
    packetNumber = packet[0][0].attrib['show']
    packetArrival = packet[0][3].attrib['show']

    for proto in packet:
        for field in proto:
            if field.attrib['name'] == "http.file_data":
                for infos in RawPacket(field.attrib['show']):
                    worksheet.write(row, col+0, packetNumber)
                    worksheet.write(
                        row, col+1, packetArrival.strip("Västeuropa, normaltid"))
                    worksheet.write(row, col+2, CstLabel(infos))
                    worksheet.write(row, col+3, CstLabels(infos))
                    worksheet.write(row, col+4, VehicleModel(infos))
                    worksheet.write(row, col+5, CarTypes(infos))
                    worksheet.write(row, col+6, BlockId(infos))
                    worksheet.write(row, col+7, DrivingDirection(infos))
                    worksheet.write(row, col+8, CurrentStationID(infos))
                    worksheet.write(row, col+9, CurrentStation(infos))
                    worksheet.write(row, col+10, NextStation(infos))
                    worksheet.write(row, col+11, NextStationID(infos))
                    worksheet.write(row, col+12, DistanceToNextStationM(
                        infos))
                    worksheet.write(row, col+13, DestinationStation(infos))
                    worksheet.write(row, col+14, DestinationStationID(
                        infos))
                    worksheet.write(row, col+15, DoorOpen(infos))
                    worksheet.write(row, col+16, DoorsClosed(infos))
                    worksheet.write(row, col+17, HasChanged(infos))
                    worksheet.write(row, col+18, LastUpdated(infos))
                    worksheet.write(row, col+19, MaxNumberOfStreams(infos))
                    row += 1

false_format = workbook.add_format({'bg_color': '#f5c4c4'})
worksheet.conditional_format('P1:R10000', {'type':     'cell',
                                           'criteria': '==',
                                           'value':    '"false"',
                                           'format':   false_format})
true_format = workbook.add_format({'bg_color': '#c1f5c1'})
worksheet.conditional_format('P1:R10000', {'type':   'cell',
                                           'criteria': '==',
                                           'value':    '"true"',
                                           'format':   true_format})

worksheet.autofilter('C1')


workbook.close()
