# DB2Rest

DB2Rest is a tool that performs integration between legacy databases and RESTful web services. The tool reads the database structure from a configuration file, in JSON, that describes the correspondence between the database entities and the SQLAlchemy templates expected by the server.


## Getting Started



### Prerequisites

What things you need to install the software and how to install them

```
Python 3.5 or superior

```
### Installing

To install the tool, use pip:

```
pip install db2rest-tool
```

Setup the environment variables in the terminal:

```
export APP_SETTINGS="config.DevelopmentConfig"
```
Setup the variable 'DATABASE_URL' to indicate the path to the Database. To learn how to create a path to your base, see the [documentation defined by SQLAlchemy](http://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls)
Examples on SQLite and Postgresql below

SQLite: 
```
export DATABASE_URL="sqlite:///test.db" #Example of one sqLite database. If not exists, the database is created.
```
Postgresql:
```
export DATABASE_URL="postgresql://<<<usuario>>>:<<<senha>>>@localhost/<<<DATABASE>>>"  #Replace the values between <<< >>>
```

Setup the environment variable 'CONFIG_FILE' with the JSON expected
```
export CONFIG_FILE="YOURFILE.json"
```

## Configuring the JSON File

Enter the values in the configuration json, according to the instructions below. 

##Configuring Models:

The fields preceding "rst" area to identify the models on web service and "db" represent the Legacy Database fields.
```json
{
  "__rst_model_name__": "Postagem", 
  "__db_table_name__": "post" 
}
```
**"__rst_model_name__"** The name of the Model on Web Service

**"__db_table_name__"** The table on the Legacy Database

### Configuring Attributes:

Following our first example, learn how to configure the attributes that are mapped.
!Atention: The attributes that are key to relationships are not in this section, but in the relationships section

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



## Configure Relationships:

This tool is based on SQLALChemy Framework. The Framework define one especific way to map relationships, and is our job generate the code expected to Framework. For do that, some fields are required acording of each type of relationship.

Pay close attention to each attribute and what it serves, as this will have a direct impact on the generated code.

Following our first example... just enter one more key "relationships" in json.

Attributes used on realitons: Many-to-One (M2O), One-to-Many(O2M) e One-to-One(O2O)

**"relationships"** JSON list with relationships from this model

**"type"** #M2O means Many-to-One relationship

**"rst_referencing_name"** The name of the field used on web service to get the relation (example: postagem.categoria)

**"rst_referenced_model** Model of the web service with which it relates

**"db_referenced_table"** The table on the database represented by the model relates.

**"db_referenced_table_pk"** The attribute primary key on referenced table (TABLE.PRIMARYKEY)

**"db_referencing_table_fk"** The attribute on this model that used as foreign key 

**"rst_referenced_backref"** The attribute that allow to acess this model by other side of relatinship (example: categoria.postagens)



###### #Many-to-One (M2O)

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
                  }],
  
  "relationships": [{
                    "type":"M2O",
                    "rst_referencing_name": "categoria",
                    "rst_referenced_model": "Categoria",
                    "db_referenced_table":"category",
                    "db_referenced_table_pk": "category.id",
                    "db_referencing_table_fk": "category",
                    "rst_referenced_backref": "postagens"}
                ]
}
```

###### #One-to-Many (O2M)

```json
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
                  
                  ],
  "relationships": [{
                    "type":"O2M",
                    "rst_referencing_name": "livro",
                    "rst_referenced_model": "Livro",
                    "db_referenced_table":"books",
                    "db_referenced_table_pk": "books.id",
                    "db_referencing_table_fk":"book_id",
                    "rst_referenced_backref":"revisao"} 
                ]
}

```

###### #One-to-One(O2O)

```json
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
                
                ],
"relationships": [{
                    "type":"O2O",
                    "rst_referencing_name": "usuario",
                    "rst_referenced_model": "Usuario",
                    "db_referenced_table":"users",
                    "db_referenced_table_pk": "users.id",
                    "db_referencing_table_fk":"user_id",
                    "rst_referenced_backref": "endereco"} 
              ]
}
```

###### #Many-to-Many (M2M)

```json
{
  "__rst_model_name__": "EntryTag",
  "__db_table_name__": "entrytag",
  "attributes": [{
                    "rst_attribute_name": "id_entrytag",
                    "db_column_table":"id",
                    "db_primary_key": "True"
                  }],
  "relationships": [{ 
                  "type":"M2M",
                  "rst_referenced_model_left":"EntryModel",
                  "rst_referenced_model_right":"TagModel",
                  "db_referenced_table_left_pk": "entry.id",
                  "db_referenced_table_right_pk": "tag.id",
                  "rst_referencing_name_left": "entry",
                  "rst_referencing_name_right": "tag",
                  "rst_referenced_backref_left":"tags",
                  "rst_referenced_backref_right":"entries"
                }
                ]
}
```


**"relationships"** JSON list with relationships from this model

**"type"** #M2M means Many-to-Many relationship

**"rst_referenced_model_left"** #The model referenced on the left of relationship

**"rst_referenced_model_right** #The model referenced on the right of relationship

**"db_referenced_table_left_pk"** #The model referenced on the left of relationship

**"db_referenced_table_right_pk"** #The model referenced on the right of relationship

**"rst_referencing_name_left"** #The attribute primary key on referenced table left

**"rst_referencing_name_right"** #The attribute primary key on referenced table left

**"rst_referenced_backref_left"** The attribute that allow to acess the list of right side on left side 

**"rst_referenced_backref_right"** The attribute that allow to acess the list of left side on right side


### Configuring Derived Attribute:

Derived attributes are nothing more than attributes that will be inserted into the template whose values are defined in a different table that has been mapped.

```json
 "derived_attributes":[{
                      "rst_property_name": "detalhes_categoria",
                      "db_columns": "category.name",
                      "db_clause_where": "id|1",
                      "db_rows_many": "False"
                        }]
```                        


### Running

Now, all that you have to do is execute the script that will read the file configuration and will generate the models that will make the adaptation between the web service interface and the legacy database.

Simply put in the terminal:

```
execute_db2rest
```

If you wrote the configuration file correctly, the models will be generated and a success message will be displayed on the terminal.

To use the models generated by Db2Rest, just import them on your services.
```
from DB2Rest import models
```


## Running the example

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
pip install -r examples/requirements.txt
```

Setup the environment variables in the terminal

```
export APP_SETTINGS="config.DevelopmentConfig"
```
SQLite: 
```
export DATABASE_URL="sqlite:///test.db" #Example of one sqLite database. If not exists, the database is created.
```

### Running

Execute script to generate models

```
execute_db2rest
```

Import the model.py on the services
```
from DB2Rest import models
```

Run the main python module

```
python run.py
```

## Authors

See also the list of [contributors](https://github.com/oliveirabrunoa/map2rest/contributors) who participated in this project.

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details
