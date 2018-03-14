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

### Configuring

Enter the values in the configuration json, according to the instructions below. 

#Configuring Models:

The fields preceding "rst" area to identify the models on web service and "db" represent the Legacy Database fields.
```json
{
  "__rst_model_name__": "Postagem", 
  "__db_table_name__": "post" 
}
```
**"__rst_model_name__"** The name of the Model on Web Service

**"__db_table_name__"** The table on the Legacy Database

#Configuring Attributes:

Following our first example, learn how to configure the attributes that are mapped.
```json
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
                     }
                  ]
}
```

**"__rst_model_name__"** The name of the Model on Web Service

**"__db_table_name__"** The table on the Legacy Database

**"attributes"** JSON list of all attributes expected

**"rst_attribute_name"** Attribute expected by Web Service

**"db_column_table"** Column of the database that will be represented on Web Service

**"db_primary_key"** Especial field that indicates that field is a primary key.

**"rst_attribute_name"** Attribute expected by Web Service

**"db_column_table"** Column of the database that will be represented on Web Service



##Configure Relationships:

This tool is based on SQLALChemy Framework. The Framework define one especific way to map relationships, and is our job generate the code expected to Framework. For do that, some fields are required acording of each type of relationship.

Pay close attention to each attribute and what it serves, as this will have a direct impact on the generated code.

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
                  "type":"M2O", #M2O means Many-to-One relationship
                  "rst_model_name": "categoria", #The name of the field used on web service to get the relation (example: postagem.categoria)
                  "rst_model_target": "UserType", # Model of the web service with which it relates
                  "db_table_name":"category", #db_table_name is The table on the database with which this model relates.
                  "db_foreign_key": "category.id", # db_foreign_key is The attribute foreign key references on the database 
                  "rst_backref": "postagens"} # rst_backref is The attribute that allow to acess this model by other side of relatinship (example: categoria.postagens)
                ]
}
```

#One-to-Many (O2M)

```
{
  "__rst_model_name__": "Revisao",
  "__db_table_name__": "reviews",
  "attributes": [{
                    "rst_attribute_name": "id",
                    "db_column_table":"id",
                    "db_primary_key": "True"
                  },
                  {
                    "rst_attribute_name":  "revisor_name",
                    "db_column_table":"reviewer_name"
                  }
                  .... more fields
                  ],
  "relationships": [{
                  "type":"O2M", #O2M means One-to-many relationship
                  "rst_model_name": "revisao", #This attribute is the name of the field that will be include in the other side of the relationship.
                  "rst_model_target": "Livro", # Model of the web service with which it relates
                  "db_table_name":"books", #db_table_name is The table on the database with which this model relates.
                  "db_foreign_key": "books.id", # db_foreign_key is The attribute foreign key references on the database 
                  "db_column_fk":"book_id", #Name of field that represente the relationship on this model.
                  "rst_back_populates":"endereco"} # Name of field that represente the "back_populates", alow acess across other side of relationship. 
                ]
}

```

#One-to-One(O2O)

```
{
"__rst_model_name__": "Endereco",
"__db_table_name__": "addresses",
"attributes": [{
                  "rst_attribute_name": "id_endereco",
                  "db_column_table":"id",
                  "db_primary_key": "True"
                },
                {
                  "rst_attribute_name":  "rua",
                  "db_column_table":"street"
                }
                ....more fields
                ],
"relationships": [{
                "type":"O2O", #O2O means One-to-One relationship
                "rst_model_name": "usuario", 
                "rst_model_target": "Usuario", # Model of the web service with which it relates
                "rst_model_target_name":"endereco", # Attribute that will be included on model target
                "db_table_name":"users",
                "db_foreign_key": "users.id",
                "db_column_fk":"user_id",
                "rst_back_populates": "endereco"} # Name of field that represente the "back_populates", alow acess across other side of relationship. 
              ]
}
```

#Many-to-Many (M2M)

```
{
  "__rst_model_name__": "EntryTag",
  "__db_table_name__": "entrytag",
  "attributes": [{
                    "rst_attribute_name": "id_entrytag",
                    "db_column_table":"id",
                    "db_primary_key": "True"
                  }],
  "relationships": [{ #Here, the letters A and B will be used to represente the right and left sids of relationship.
                  "type":"M2M", #M2M means Many-to-Many relationship
                  "rst_association_a":"EntryModel", # Model of the web service that represent left side
                  "rst_association_b":"TagModel", #Model of the web service that represent right side
                  "db_association_fk_a": "entry.id", # The attribute foreign key references on the database, left
                  "db_association_fk_b": "tag.id", # The attribute foreign key references on the database, right
                  "rst_association_atribute_a": "entry", #atribute that represents the relation on left side
                  "rst_association_atribute_b": "tag", #atribute that represents the relation on left side
                  "rst_back_populates_a":"tags", # Name of field that represente the "back_populates", alow acess across other side of relationship, across left
                  "rst_back_populates_b":"entries" # Name of field that represente the "back_populates", alow acess across other side of relationship, across right
                }
                ]
}
```

### Running

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
