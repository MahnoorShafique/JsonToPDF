import fpdf as fpdf
import json
from rest_framework import viewsets
from rest_framework.response import Response


class Abc(viewsets.ViewSet):

    def list1(self, request):
        with open('Portfolio Refactored Mahnoor.postman_collection.json', 'r') as infile:
            contents = json.load(infile)  # Parse JSON data into a Python object. (A)
            print(contents)

        pdf = fpdf.FPDF(format='letter')
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        mydict = {}
        try:
            for x in range(len(contents['item'])):
                api_name = contents['item'][x]['name']

                pdf.cell(200, 10, txt=" API For " + api_name, ln=1, align='C')
                pdf.cell(10, 10, txt="Name                       " + "      Url", ln=1)
                mynewlist = []
                for y in contents['item'][x]['item']:
                    name = y['name']
                    url = [y['request']['url']['raw']]
                    mynewlist.append([{name: url}])
                    mydict[api_name] = mynewlist
                    pdf.write(10, str(name) + "   ---->  ")
                    pdf.write(10, "      " + str(url))
                    pdf.ln()

                pdf.add_page()

            pdf.output("testings.pdf")

            response = {"data": mydict,

            }
            return Response(response)
        except Exception as e:
            response = {

                'message': str(e)

            }
            return Response(response)  # return str(e)

