# DB2Rest

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project in the live system.

### Prerequisites

What things you need to install the software and how to install them

```
Python 3.5 or superior

You need to install a DB(SqLite, PostgreSQL) of your choice to create the tables and to invoke services.
```

### Installing

Create the python virtualenv

```
python3 -m venv myvenv
```

Active the virtualenv

```
source myvenv/bin/activate
```

Install project requirements save in requirements.txt

```
pip install -r requirements.txt
```

Setup the environment variables in the terminal

```
export APP_SETTINGS="config.DevelopmentConfig"
```
SQLite: 
```
export DATABASE_URL="sqlite:///test.db" #Example of one sqLite database. If not exists, the database is created.
```
Postgresql:
```
export DATABASE_URL="postgresql://<<<usuario>>>:<<<senha>>>@localhost/<<<DATABASE>>>"  #Replace the values between <<< >>>
```

### Running

Enter the values in the configuration json, according to the instructions below. 

#Configuring Models:

The fields preceding "rst" area to identify the models on web service and "db" represent the Legacy Database fields.
```
{
  "__rst_model_name__": "Postagem", #The name of the Model on Web Service
  "__db_table_name__": "post", #The table on the Legacy Database
}
```

#Configuring Attributes:

Following our first example, learn how to configure the attributes that are mapped.
```
{
  "__rst_model_name__": "Postagem", #The name of the Model on Web Service
  "__db_table_name__": "post", #The table on the Legacy Database
  "attributes": [{ # JSON list of all attributes expected
                      "rst_attribute_name": "id_postagem", #Attribute expected by Web Service
                      "db_column_table":"id", #Column of the database that will be represented on Web Service
                      "db_primary_key": "True" #Especial field that indicates that field is a primary key.
                    },
                    {
                      "rst_attribute_name":  "titulo", #Attribute expected by Web Service
                      "db_column_table":"title" #Column of the database that will be represented on Web Service
                     }
                  ]
}
```
##Configure Relationships:

This tool is based on SQLALChemy Framework. The Framework define one especific way to map relationships, and is our job generate the code expected to Framework. For do that, some fields are required acording of each type of relationship.

Following our first example... just enter one more key "relationships" in json.

#Many-to-One (M2O)

```
{
  "__rst_model_name__": "Postagem",
  "__db_table_name__": "post",
  "attributes": [{
                    "rst_attribute_name": "id_postagem",
                    "db_column_table":"id",
                    "db_primary_key": "True"
                  },
                  {
                    "rst_attribute_name":  "titulo",
                    "db_column_table":"title"
                  }],
  
  "relationships": [{
                  "type":"M2O", #M2O means Many-to-many relationship
                  "rst_model_name": "categoria", #The name of the field used on web service to get the relation (example: postagem.categoria) 
                  "db_table_name":"category", #db_table_name is The table on the database with which this model relates.
                  "db_foreign_key": "category.id", # db_foreign_key is The attribute foreign key references on the database 
                  "rst_backref": "postagens"} # rst_backref is The attribute that allow to acess this model by other side of relatinship (example: categoria.postagens)
                ]
}
```





Execute script to generate models

```
python execute_map2rest.py
```

Run the main python module

```
python run.py
```

## Authors

See also the list of [contributors](https://github.com/oliveirabrunoa/map2rest/contributors) who participated in this project.

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details
