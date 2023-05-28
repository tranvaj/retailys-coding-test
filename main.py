from xml.dom import minidom as dom


def main():
    msg = ""
    xmldoc = dom.parse("export_full.xml")
    items = xmldoc.documentElement.getElementsByTagName("item")
    msg += "Pocet produktu: " + str(len(items)) + "\n"

    for item in items:
        msg += "Nazev produktu: " + item.getAttribute("name") + "\n"
        parts = item.getElementsByTagName("part")
        if parts:
            for part in parts:
                sub_parts = part.getElementsByTagName("item")
                for sub_part in sub_parts:
                    sub_part_name = sub_part.getAttribute("name")
                    msg += "\tNahradniho dilo: " + sub_part_name + "\n"

    print("Psani do souboru")
    f = open('output.txt', 'w', encoding="utf-8")
    f.write(msg)
    f.close()



main()
