
# coding: utf-8

from pycti import OpenCTIApiClient

# Variables
api_url = ""
api_token = ""

# OpenCTI initialization
opencti_api_client = OpenCTIApiClient(api_url, api_token)


StixCoreObjectOrStixCoreRelationshipLastReportsQuer = '''
query StixCoreObjectOrStixCoreRelationshipLastReportsQuery(
  $first: Int  # 定義查詢結果中第一個要返回的元素數量
  $orderBy: ReportsOrdering  # 定義按照什麼屬性排序
  $orderMode: OrderingMode  # 升幕或降幕
  $filters: [ReportsFiltering]  # 定義過濾器
) {
  reports(first: $first, orderBy: $orderBy, orderMode: $orderMode, filters: $filters) {
    edges {
      node {
        id  #  ID
        name  # 標題
        description  # 描述
        published  # 發布時間
        createdBy {  # 創建者資料
          __typename
          __isIdentity: __typename
          id
          name
          entity_type
        }
        objectMarking {  # 就是 tlp
          edges {
            node {
              definition
              id
            }
          }
        }
      }
    }
  }
}

'''

#just replace filters value with your own
results = opencti_api_client.query(StixCoreObjectOrStixCoreRelationshipLastReportsQuer,variables={"first":8,"orderBy":"published","orderMode":"desc","filters":[{"key":"objectContains","values":["3e35d767-d8e8-4bde-beb7-3c2e1ba7687b"]}]})

print(results)
