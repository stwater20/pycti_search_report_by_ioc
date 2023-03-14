# pycti_search_report_by_ioc


opencti Version: 5.3.17

In short, 
the StixCoreObjectOrStixCoreRelationshipLastReportsQuery is not available in Pycti, 
although it is documented on the website. 

At the time of writing, the Pycti documentation was empty, 
so I hope this can help those who want to use OpenCTI.

## I'll shoulder the burden of my suffering 


If possible, please visit https://sectools.tw ...

一袋米要扛幾樓...

## How to use

Just change the values to the ioc that you want to search

<code>
  opencti_api_client.query(StixCoreObjectOrStixCoreRelationshipLastReportsQuer,variables={"first":8,"orderBy":"published","orderMode":"desc","filters":[{"key":"objectContains","values":["3e35d767-d8e8-4bde-beb7-3c2e1ba7687b"]}]})

</code>
