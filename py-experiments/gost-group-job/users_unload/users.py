import argparse
import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser()

PSD_CREDITNAILS = os.getenv("PSD_CREDITNAILS")
ETS_CREDITNAILS = os.getenv("ETS_CREDITNAILS")
START1 = "2019-12-31"
START2 = "2021-09-01"
END = "2021-09-30"


psd_all_active_users = """ SELECT COUNT(*)
                           FROM public.res_users
                           WHERE "active" is true
"""

psd_uniq_users_for_dates = """ SELECT COUNT(*)
                           FROM public.res_users u
                           INNER join (
                           SELECT create_uid id, max(create_date) last_date
                           FROM public.res_users_log
                           where "create_date" BETWEEN '{}' AND '{}'
                           GROUP BY "create_uid") l
                           on u.id = l.id
                           inner join (SELECT id, "name"
                           FROM public.res_partner) name on partner_id = name.id
                           where active = '1';
"""

ets_all_active_users = """ SELECT COUNT(*)
                           FROM ets."USER"
                           Where role_id != 79 and is_deleted is false;
"""

ets_uniq_users_for_dates = """ select COUNT(*)
                               from ets."USER" u
                               inner join (select al."user_id" as user_id, max(al."action_at"::date) as last_action_date
                               from ets."user_action_log" al
                               where al."action_at" between '{}' and '{}'
                               group by al."user_id") as log
                               on log.user_id = u."ID";
"""


def get_psd_results():
    con = psycopg2.connect(PSD_CREDITNAILS)
    cur = con.cursor()

    cur.execute(psd_all_active_users)
    all_active_users = cur.fetchall()

    cur.execute(psd_uniq_users_for_dates.format(START1, END))
    uniq_users_for_dates1 = cur.fetchall()

    cur.execute(psd_uniq_users_for_dates.format(START2, END))
    uniq_users_for_dates2 = cur.fetchall()

    return [
        "ПСД\n",
        "Всего пользователей: " + str(all_active_users[0][0]) + "\n",
        "За даты:\n",
        START1 + "-" + END + ": " + str(uniq_users_for_dates1[0][0]) + "\n",
        START2 + "-" + END + ": " + str(uniq_users_for_dates2[0][0]) + "\n",
    ]


def get_ets_results():
    con = psycopg2.connect(ETS_CREDITNAILS)
    cur = con.cursor()

    cur.execute(ets_all_active_users)
    all_active_users = cur.fetchall()

    cur.execute(ets_uniq_users_for_dates.format(START1, END))
    uniq_users_for_dates1 = cur.fetchall()

    cur.execute(ets_uniq_users_for_dates.format(START2, END))
    uniq_users_for_dates2 = cur.fetchall()

    return [
        "ЕТС\n",
        "Всего пользователей:" + str(all_active_users[0][0]) + "\n",
        "За даты:\n",
        START1 + "-" + END + ": " + str(uniq_users_for_dates1[0][0]) + "\n",
        START2 + "-" + END + ": " + str(uniq_users_for_dates2[0][0]) + "\n",
    ]


def main():
    data = get_psd_results() + get_ets_results()
    with open("./result/output.txt", "w") as output:
        output.writelines(data)
    print("Готово")


main()
