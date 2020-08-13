import boto3
import boto3.session
import sys
import yaml

my_session=""
AWS_SERVER_PUBLIC_KEY=""
AWS_SERVER_SECRET_KEY=""

def aws_configuration(account):
    ##with open("./config/config.yml", "r") as ymlfile:
    cfg = yaml.load(open("./config/config.yml"),Loader=yaml.FullLoader)
    print(f'Full YAML File:{cfg}')
    for k,v in cfg.items():
        print(k)
        if k == account[0]:
            AWS_SERVER_PUBLIC_KEY=v[0]['aws_access_key_id']
            AWS_SERVER_SECRET_KEY=v[1]['aws_secret_access_key']
            print (f'{AWS_SERVER_PUBLIC_KEY}     {AWS_SERVER_SECRET_KEY}')
        else:
            print(f'yamls file in {k}')
    return AWS_SERVER_PUBLIC_KEY,AWS_SERVER_SECRET_KEY
   
### Function to List the buckets 
def lists3buckets(account):
    aws_access_key_id,aws_secret_access_key=aws_configuration(account)
    s3 = boto3.client ('s3',aws_access_key_id = aws_access_key_id,aws_secret_access_key = aws_secret_access_key,region_name = 'ap-southeast-2')
    i=0
    response =s3.list_buckets()
    ### Listing the buckets from the response which is a Dictionary
    for response_dict in response.get('Buckets'):
        print(response_dict['Name'])
if __name__== "__main__":
    globals()[sys.argv[1]]([sys.argv[2]])
