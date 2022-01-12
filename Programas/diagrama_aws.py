# diagrams==0.19.1
# graphviz==0.16
# Jinja2==2.11.3
# MarkupSafe==1.1.1
# Para rodar basta fazer um Git Clone e
# em seguida rodar "pip install -r requirements.txt"
# pip3 install diagrams
# pip3 install graphviz


from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS,   EKS, Lambda
from diagrams.aws.database import Elasticache, RDS, Redshift
from diagrams.aws.integration import SQS
from diagrams.aws.network import ELB, Route53
from diagrams.aws.storage import S3
from diagrams.aws.security import WAF

with Diagram("AWS", show=False):

    source = EKS("EKS SOURCE")
    with Cluster("Região"):
        awf = WAF("AWF")

        with Cluster("event flows"):
            with Cluster("event web"):
                svc_group = [ECS("web1"),
                             ECS("web2"),
                             ECS("web3"),
                             ECS("web3")]

        queue = SQS("event queue")

        with Cluster("Processing"):
            handlers = [Lambda('pro1'),
                        Lambda('pro2'),
                        Lambda('pro3')]

    storage = S3("Event store")
    dw = Redshift("analystics")

    awf >> source >> svc_group >> queue >> handlers
    handlers >> storage
    handlers >> dw
