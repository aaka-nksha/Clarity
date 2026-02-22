import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

class AnalyticsProcessor:
    def __init__(self):
        # Set environment variables for Windows compatibility
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        hadoop_path = os.path.join(project_root, "hadoop")
        
        os.environ["HADOOP_HOME"] = hadoop_path
        # Ensure JAVA_HOME points to a valid JDK (fixing potential bin suffix issue)
        if "JAVA_HOME" not in os.environ or "bin" in os.environ["JAVA_HOME"]:
             # Try to find a standard JDK path if not set correctly
             standard_java = r"C:\Program Files\Java\jdk-17"
             if os.path.exists(standard_java):
                 os.environ["JAVA_HOME"] = standard_java
        
        # Add hadoop bin to PATH
        hadoop_bin = os.path.join(hadoop_path, "bin")
        if hadoop_bin not in os.environ["PATH"]:
            os.environ["PATH"] = hadoop_bin + os.pathsep + os.environ["PATH"]

        try:
            self.spark = SparkSession.builder \
                .appName("ClarityAnalytics") \
                .config("spark.driver.host", "localhost") \
                .config("spark.sql.warehouse.dir", os.path.join(project_root, "spark-warehouse")) \
                .getOrCreate()
            print("Spark Session initialized successfully.")
        except Exception as e:
            print(f"Spark not initialized: {e}")
            self.spark = None

    def analyze_productivity_trends(self, events_df):
        """
        Example PySpark function to analyze productivity data.
        """
        if not self.spark:
            return "Spark not available."
            
        # Group by goal type and calculate average completion time
        trends = events_df.groupBy("goal_type") \
            .avg("completion_time") \
            .orderBy(col("avg(completion_time)").desc())
            
        return trends.collect()
