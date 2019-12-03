WIKIDATA_REQUEST1 ="""SELECT DISTINCT ?item ?itemLabel ?image ?value ?valueLabel
WHERE
{
  ?item wdt:P2040 ?value;
        rdfs:label ?itemLabel .
  OPTIONAL { ?item wdt:P18 ?image. }      
  FILTER(CONTAINS(LCASE(?itemLabel), """

WIKIDATA_REQUEST2 = """))
  FILTER (LANG(?itemLabel)="fr") }"""

