import mysql.connector
import os

def create_connection(db_name):
    
    db_conn = mysql.connector.connect(
        host=os.getenv("MARIA_HOST"),
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

def load_distribution_v2():
    conn = create_connection(db_name="pekerjaan")
    cursor = conn.cursor()
    sql = "select distribusi.daerah_id, daerah.nama_kelurahan, daerah.nama_kecamatan, daerah.nama_kota, daerah.nama_provinsi, pekerjaan.nama, jumlah " \
        "from distribusi, pekerjaan, daerah " \
        "where distribusi.daerah_id=daerah.id and distribusi.pekerjaan_id=pekerjaan.id and distribusi.jumlah>0"
    
    cursor.execute(sql)
    results = cursor.fetchall()
    
    all_result = []
    for i in results:
        data = dict()
        data["daerah_id"] = i[0]
        data["village"] = i[1]
        data["district"] = i[2]
        data["city"] = i[3]
        data["province"] = i[4]
        data["category"] = "job"
        data["roles"] = i[5]
        data["amount"] = i[6]
        all_result.append(data)
    
    print (len(results))
    cursor.close()
    conn.close()
    
    conn = create_connection(db_name="pendidikan")
    cursor = conn.cursor()
    sql = "select distribusi.daerah_id, daerah.nama_kelurahan, daerah.nama_kecamatan, daerah.nama_kota, daerah.nama_provinsi, pendidikan.nama, jumlah " \
        "from distribusi, pendidikan, daerah " \
        "where distribusi.daerah_id=daerah.id and distribusi.pendidikan_id=pendidikan.id and distribusi.daerah_id<=20"
    
    cursor.execute(sql)
    results = cursor.fetchall()
    
    for i in results:
        data = dict()
        data["daerah_id"] = i[0]
        data["village"] = i[1]
        data["district"] = i[2]
        data["city"] = i[3]
        data["province"] = i[4]
        data["category"] = "education"
        data["roles"] = i[5]
        data["amount"] = i[6]
        all_result.append(data)
    
    print (len(results))
    cursor.close()
    conn.close()
    
    print (len(all_result))
    return sorted(all_result, key=lambda d: d['daerah_id'])

if __name__=="__main__":
    # handle_region()
    # print(load_educations())
    # print(load_jobs())
    
    # print (load_distribution()[-1])    
    # print (len(load_distribution()))
    
    load_distribution_v2()
    