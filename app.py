import pandas as pd

def get_type_test_and_place(started_data):
  type_test_and_place = ( started_data
                         .iloc[1]
                         .str.replace(r'\s+', ' ', regex=True)
                         .str.split(r'EXAMEN\s\DE\sADMISION\s|\sP', expand=True)
                         .loc['raw_data', 1]
                         )
  return type_test_and_place

def get_date(started_data):
  date = (started_data
          .iloc[2]
          .str.extract(r'(\d+/\d+/\d+)')
          .loc['raw_data', 0]
          )
  
  return date

def get_row_area(started_data):
  row_area = (started_data
              .iloc[2]
              .str.replace(r'\s+', ' ', regex=True)
              ['raw_data']
              )
  
  return row_area

def remove_extra_spaces_from_df(started_data):
  filter_rows = ( started_data
               ['raw_data']
               .map(lambda row: row.startswith(' 0'))
               )

  without_extra_spaces_S = ( started_data
                            .loc[filter_rows]
                            .reset_index()
                            .drop('index', axis=1)
                            ['raw_data']
                            .str.replace(r'\s+', ' ', regex=True)
                            .str.strip()
                            )
  
  return without_extra_spaces_S

def get_full_name(without_extra_spaces_s):
  full_name_df = ( without_extra_spaces_s
                  .str.extract(r'(\s\D+\s-?\d)')
                  [0]
                  .str.replace(r'-?\d', '', regex=True)
                  )
  
  return full_name_df

def get_grades(without_extra_spaces_s):
  grades_df = ( without_extra_spaces_s
               .str.extractall(r'(-?\d+\.\d+)')
               .unstack()
               )
  
  grades_df.columns = grades_df.columns.droplevel(0)
  grades_df.columns = grades_df.columns.rename(name=None)

  return grades_df

def get_school_with_details(without_extra_spaces_s):
  school_with_detail_S = ( without_extra_spaces_s
                          .str.extract(r'(\.\d+\s[A-Z].*)')
                          [0]
                           .str.replace(r'\.\d+\s', '', regex=True)
                           )
  
  return school_with_detail_S

def get_details(school_plus_detail_s):
  details_S = ( school_plus_detail_s
               .str.extract(r'(INGRESA.*|NO\sINGRESA.*|ING\.\s?2.*|AUSENTE.*|ANULADO.*)')
               [0]
               )
  
  return details_S

def get_school(school_plus_detail_s):
  school_S = ( school_plus_detail_s
              .str.replace(r'INGRESA.*|NO\sINGRESA.*|ING\.\s?2.*|AUSENTE.*|ANULADO.*', '', regex=True)
              )
  return school_S

def join_data(full_name, grades, school, details, date, type_and_place, row_area):
  final_df = pd.concat(
    [full_name, grades, school, details]
    ,axis='columns'
    ,sort=False
    )

  final_df.columns = ['full_name', 'apt_academica', 'conocimiento', 'total', 'minimo', 'escuela', 'observacion']

  final_df['date'] = date
  final_df['row_area'] = row_area
  final_df['type_test_and_place'] = type_and_place

  return final_df

def transform_data(initial_data):
  test_and_place = get_type_test_and_place(initial_data)
  date = get_date(initial_data)
  row_area = get_row_area(initial_data)

  without_extra_spaces = remove_extra_spaces_from_df(initial_data)
  
  full_name = get_full_name(without_extra_spaces)
  grades = get_grades(without_extra_spaces)

  school_plus_details = get_school_with_details(without_extra_spaces)
  school = get_school(school_plus_details)
  detail = get_details(school_plus_details)

  result_df = join_data(full_name, grades, school, detail, date, test_and_place, row_area)

  return result_df

def get_data(url):
  initial_data = pd.read_csv(url,
                 encoding='ISO-8859-1',
                 names= { 'raw_data': 0 }
                 )
  
  return initial_data

def main():

  data_url = {
  'url1' : 'https://unitru.edu.pe/webfiles///Convocatoria/2023/3//73_DOC_CONVO_260320230625.txt',
  'url2' : 'https://unitru.edu.pe/webfiles///Convocatoria/2023/3//73_DOC_CONVO_260320230621.txt',
  'url3' : 'https://unitru.edu.pe/webfiles///Convocatoria/2023/3//73_DOC_CONVO_260320230619.txt',
  'url4' : 'https://unitru.edu.pe/webfiles///Convocatoria/2023/3//73_DOC_CONVO_260320230551.txt',
  'url5' : 'https://unitru.edu.pe/webfiles///Convocatoria/2023/3//73_DOC_CONVO_250320230733.txt',
  'url6' : 'https://unitru.edu.pe/webfiles///Convocatoria/2023/3//73_DOC_CONVO_250320230635.txt',
  'url7' : 'https://unitru.edu.pe/webfiles///Convocatoria/2023/3//73_DOC_CONVO_250320230631.txt',
  'url8' : 'https://unitru.edu.pe/webfiles///Convocatoria/2023/3//73_DOC_CONVO_240320230541.txt',
  'url9' : 'https://unitru.edu.pe/webfiles///Convocatoria/2023/3//73_DOC_CONVO_240320230533.txt',
  'url10' : 'https://unitru.edu.pe/webfiles///Convocatoria/2023/3//73_DOC_CONVO_240320230530.txt',
  }

  results = []
  
  for url in data_url.values():
    initial_data = get_data(url)
    result = transform_data(initial_data)
    results.append(result)

  final = pd.concat(results, axis=0, sort=False)

  return final

if __name__ == '__main__':
  main()