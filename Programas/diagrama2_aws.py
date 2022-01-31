# diagrams==0.19.1
# graphviz==0.16
# Jinja2==2.11.3
# MarkupSafe==1.1.1
# Para rodar basta fazer um Git Clone e
# em seguida rodar "pip install -r requirements.txt"
# pip3 install diagrams
# pip3 install graphviz

from http import client
from diagrams.aws.general import Users
from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS,   EKS, Lambda,EC2Instance
from diagrams.aws.database import Elasticache, RDS, Redshift
from diagrams.aws.integration import SQS
from diagrams.aws.network import ELB, Route53, InternetGateway, ALB
from diagrams.aws.storage import S3
from diagrams.aws.security import WAF

with Diagram("AWS", show=False):

    source = Users("Users")
    with Cluster("South America(São Paulo)"):
        with Cluster("VPC"):
            internet = InternetGateway("Internet\nGateway")
            applb = ALB("Application\nLoad Balancer")

            with Cluster("Public\nSubnet"):
                with Cluster("Cluster EKS"):
                    eks_group =[ECS("3 instâncias\nt3a.medium")]
                ec2_group =[EC2Instance("t3a.small"), 
                            EC2Instance("t3a.medium")]

            with Cluster("Private\nSubnet"):
                     rds_group = [RDS('pro1'),
                                RDS('db.t3 large')]

    

    source >> internet >> applb 
    applb >> eks_group
    applb >> rds_group
   
    
    
    