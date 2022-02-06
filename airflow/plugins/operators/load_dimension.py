from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 # Define your operators params (with defaults) here
                 # Example:
                 # conn_id = your-connection-name
                 redshift_conn_id="",
                 table="",
                 sql_stmt="",
                 append=False,
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        # Map params here
        # Example:
        # self.conn_id = conn_id
        self.redshift_conn_id=redshift_conn_id
        self.table=table
        self.sql_stmt=sql_stmt
        self.append=append

    def execute(self, context):
        self.log.info('Connect to Redshift')
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
        if self.append == False:
            self.log.info(f"Delete table {self.table}")
            redshift.run(f"DELETE FROM {self.table}")
                       
        self.log.info(f"Load data from S3 to Redshift into Dimension Table {self.table}")
        redshift.run(f"INSERT INTO {self.table} {self.sql_stmt}")
        self.log.info(f"Table {self.table} successfully loaded.")
        
