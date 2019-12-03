WIKIDATA_REQUEST1 ="""SELECT DISTINCT ?item ?itemLabel ?value  ?valueLabel
WHERE
{
  ?item wdt:P2040 ?value;
        rdfs:label ?itemLabel .
  FILTER(CONTAINS(LCASE(?itemLabel), """

WIKIDATA_REQUEST2 = """))
  FILTER (LANG(?itemLabel)="fr") }"""

