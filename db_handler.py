from unittest import result
import mysql.connector

def create_connection(db_name):
    
    db_conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mypass",
        database=db_name
    )

    if not db_conn.is_connected():
        print("Failed connect to database")
    return db_conn

def load_distribution():
    conn = create_connection(db_name="pekerjaan")
    cursor = conn.cursor()
    sql = "SELECT distribusi.daerah_id, pekerjaan.nama, jumlah FROM distribusi, daerah, pekerjaan " \
        "where distribusi.daerah_id=daerah.id and distribusi.pekerjaan_id=pekerjaan.id order by distribusi.id asc"
    cursor.execute(sql)
    results = cursor.fetchall()
    
    village_jobs = dict()
    for data in results:
        village_jobs[data[0]] = []
    
    for data in results:
        village_jobs[data[0]].append(
            dict(name=data[1], amount=data[2])
        )
        
    cursor.close()
    conn.close()
        
    conn = create_connection(db_name="pendidikan")
    cursor = conn.cursor()
    sql = "SELECT distribusi.daerah_id, pendidikan.nama, jumlah FROM distribusi, daerah, pendidikan " \
        "where distribusi.daerah_id=daerah.id and distribusi.pendidikan_id=pendidikan.id order by distribusi.id asc"
    cursor.execute(sql)
    results = cursor.fetchall()
    
    village_educs = dict()
    for data in results:
        village_educs[data[0]] = []
    
    for data in results:
        village_educs[data[0]].append(
            dict(name=data[1], amount=data[2])
        )
        
    cursor = conn.cursor()
    sql = "select id, nama_kelurahan, nama_kecamatan, nama_kota, nama_provinsi from daerah limit 20"
    cursor.execute(sql)
    results = cursor.fetchall()
    
    all_results_educations = []
    for data in results:
        result = dict()
        result["village"] = data[1]
        result["district"] = data[2]
        result["city"] = data[3]
        result["province"] = data[4]
        result["educations"] = village_educs[data[0]]
        result["jobs"] = village_jobs[data[0]]
        all_results_educations.append(result)
        # print (result)
   
    cursor.close()
    conn.close()
    return all_results_educations

if __name__=="__main__":
    # handle_region()
    # print(load_educations())
    # print(load_jobs())
    
    print (load_distribution()[-1])    
    print (len(load_distribution()))
    