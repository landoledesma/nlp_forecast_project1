import xml.etree.ElementTree as ET

def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    data = []
    for award in root.findall('Award'):
        row = {
            'AwardTitle': award.findtext('AwardTitle', default=''),
            'AbstractNarration': award.findtext('AbstractNarration', default=''),
            'Organization_Code': award.find('./Organization/Code').text if award.find('./Organization/Code') is not None else '',
            'Directorate': ' '.join(filter(None, [award.find('./Organization/Directorate/Abbreviation').text if award.find('./Organization/Directorate/Abbreviation') is not None else '',
                                                  award.find('./Organization/Directorate/LongName').text if award.find('./Organization/Directorate/LongName') is not None else ''])),
            'Division': ' '.join(filter(None, [award.find('./Organization/Division/Abbreviation').text if award.find('./Organization/Division/Abbreviation') is not None else '',
                                               award.find('./Organization/Division/LongName').text if award.find('./Organization/Division/LongName') is not None else '']))
        }
        data.append(row)
    
    return data
