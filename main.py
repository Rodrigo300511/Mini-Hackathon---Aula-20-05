from src.extract import Extract
from src.load import Load

ext = Extract()
ld = Load()

# br = ext.extract_country("Brazil")
# ld.create_sqlite_table(br, "universidades", "uni_br")
# ld.insert_in_mongo(br, "universidades", "uni_br")

# it = ext.extract_country("Italy")
# ld.create_sqlite_table(it, "universidades", "uni_it")
# ld.insert_in_mongo(it, "universidades", "uni_it")

teste = ext.extract_ibge_Hackathon()

collections = {
    "4099": "taxa_desocupacao",
    "4096": "taxa_participacao",
    "12466": "taxa_informalidade"
}

for item in teste:

    variavel_id = item.get("id")

    if variavel_id in collections:

        ld.load_ibge_to_mongo(
            item,
            db_name="ibge_database",
            collection_name=collections[variavel_id]
        )
