SimpleStixObjectOrStixRelationshipStixCoreRelationshipsLinesPaginationQuery = '''
query SimpleStixObjectOrStixRelationshipStixCoreRelationshipsLinesPaginationQuery(
  $elementId: [String]!
  $relationship_type: [String]
  $startTimeStart: DateTime
  $startTimeStop: DateTime
  $stopTimeStart: DateTime
  $stopTimeStop: DateTime
  $confidences: [Int]
  $orderBy: StixCoreRelationshipsOrdering
  $orderMode: OrderingMode
  $count: Int!
  $cursor: ID
) {
  ...SimpleStixObjectOrStixRelationshipStixCoreRelationshipsLines_data_3Yedex
}

fragment SimpleStixObjectOrStixRelationshipStixCoreRelationshipLine_node on StixCoreRelationship {
  id
  entity_type
  parent_types
  relationship_type
  confidence
  start_time
  stop_time
  description
  is_inferred
  created_at
  x_opencti_inferences {
    rule {
      id
      name
    }
  }
  from {
    __typename
    ... on StixDomainObject {
      __isStixDomainObject: __typename
      id
      entity_type
      parent_types
      created_at
      updated_at
      objectLabel {
        edges {
          node {
            id
            value
            color
          }
        }
      }
    }
    ... on AttackPattern {
      name
      description
      x_mitre_id
      killChainPhases {
        edges {
          node {
            id
            phase_name
            x_opencti_order
          }
        }
      }
      objectMarking {
        edges {
          node {
            id
            definition
          }
        }
      }
      objectLabel {
        edges {
          node {
            id
            value
            color
          }
        }
      }
      id
    }
    ... on Campaign {
      name
      description
      id
    }
    ... on CourseOfAction {
      name
      description
      id
    }
    ... on Individual {
      name
      description
      id
    }
    ... on Organization {
      name
      description
      id
    }
    ... on Sector {
      name
      description
      id
    }
    ... on System {
      name
      description
      id
    }
    ... on Indicator {
      name
      description
      id
      pattern_type
      pattern_version
      valid_from
      valid_until
      x_opencti_score
      x_opencti_main_observable_type
      created
      objectMarking {
        edges {
          node {
            id
            definition
          }
        }
      }
      objectLabel {
        edges {
          node {
            id
            value
            color
          }
        }
      }
    }
    ... on Infrastructure {
      name
      description
      id
    }
    ... on IntrusionSet {
      name
      description
      id
    }
    ... on Position {
      name
      description
      id
    }
    ... on City {
      name
      description
      id
    }
    ... on Country {
      name
      description
      id
    }
    ... on Region {
      name
      description
      id
    }
    ... on Malware {
      name
      description
      id
    }
    ... on ThreatActor {
      name
      description
      id
    }
    ... on Tool {
      name
      description
      id
    }
    ... on Vulnerability {
      name
      description
      id
    }
    ... on Incident {
      name
      description
      id
    }
    ... on Event {
      name
      description
      id
    }
    ... on Channel {
      name
      description
      id
    }
    ... on Narrative {
      name
      description
      id
    }
    ... on Language {
      name
      id
    }
    ... on StixCyberObservable {
      __isStixCyberObservable: __typename
      id
      entity_type
      parent_types
      observable_value
      objectMarking {
        edges {
          node {
            id
            definition
          }
        }
      }
      objectLabel {
        edges {
          node {
            id
            value
            color
          }
        }
      }
    }
    ... on BasicRelationship {
      __isBasicRelationship: __typename
      id
      entity_type
      parent_types
    }
    ... on StixCoreRelationship {
      relationship_type
      id
    }
    ... on Artifact {
      id
    }
    ... on AutonomousSystem {
      id
    }
    ... on BankAccount {
      id
    }
    ... on CryptocurrencyWallet {
      id
    }
    ... on CryptographicKey {
      id
    }
    ... on Directory {
      id
    }
    ... on DomainName {
      id
    }
    ... on EmailAddr {
      id
    }
    ... on EmailMessage {
      id
    }
    ... on EmailMimePartType {
      id
    }
    ... on ExternalReference {
      id
    }
    ... on Hostname {
      id
    }
    ... on IPv4Addr {
      id
    }
    ... on IPv6Addr {
      id
    }
    ... on KillChainPhase {
      id
    }
    ... on Label {
      id
    }
    ... on MacAddr {
      id
    }
    ... on MarkingDefinition {
      id
    }
    ... on MediaContent {
      id
    }
    ... on Mutex {
      id
    }
    ... on NetworkTraffic {
      id
    }
    ... on Note {
      id
    }
    ... on ObservedData {
      id
    }
    ... on Opinion {
      id
    }
    ... on PaymentCard {
      id
    }
    ... on PhoneNumber {
      id
    }
    ... on Process {
      id
    }
    ... on Report {
      id
    }
    ... on Software {
      id
    }
    ... on StixCyberObservableRelationship {
      id
    }
    ... on StixFile {
      id
    }
    ... on StixMetaRelationship {
      id
    }
    ... on StixSightingRelationship {
      id
    }
    ... on Text {
      id
    }
    ... on Url {
      id
    }
    ... on UserAccount {
      id
    }
    ... on UserAgent {
      id
    }
    ... on WindowsRegistryKey {
      id
    }
    ... on WindowsRegistryValueType {
      id
    }
    ... on X509Certificate {
      id
    }
  }
  to {
    __typename
    ... on StixDomainObject {
      __isStixDomainObject: __typename
      id
      entity_type
      parent_types
      created_at
      updated_at
      objectLabel {
        edges {
          node {
            id
            value
            color
          }
        }
      }
    }
    ... on AttackPattern {
      name
      description
      x_mitre_id
      killChainPhases {
        edges {
          node {
            id
            phase_name
            x_opencti_order
          }
        }
      }
      objectMarking {
        edges {
          node {
            id
            definition
          }
        }
      }
      objectLabel {
        edges {
          node {
            id
            value
            color
          }
        }
      }
      id
    }
    ... on Campaign {
      name
      description
      id
    }
    ... on CourseOfAction {
      name
      description
      id
    }
    ... on Individual {
      name
      description
      id
    }
    ... on Organization {
      name
      description
      id
    }
    ... on Sector {
      name
      description
      id
    }
    ... on System {
      name
      description
      id
    }
    ... on Indicator {
      name
      description
      id
      pattern_type
      pattern_version
      valid_from
      valid_until
      x_opencti_score
      x_opencti_main_observable_type
      created
      objectMarking {
        edges {
          node {
            id
            definition
          }
        }
      }
      objectLabel {
        edges {
          node {
            id
            value
            color
          }
        }
      }
    }
    ... on Infrastructure {
      name
      description
      id
    }
    ... on IntrusionSet {
      name
      description
      id
    }
    ... on Position {
      name
      description
      id
    }
    ... on City {
      name
      description
      id
    }
    ... on Country {
      name
      description
      id
    }
    ... on Region {
      name
      description
      id
    }
    ... on Malware {
      name
      description
      id
    }
    ... on ThreatActor {
      name
      description
      id
    }
    ... on Tool {
      name
      description
      id
    }
    ... on Vulnerability {
      name
      description
      id
    }
    ... on Incident {
      name
      description
      id
    }
    ... on Event {
      name
      description
      id
    }
    ... on Channel {
      name
      description
      id
    }
    ... on Narrative {
      name
      description
      id
    }
    ... on Language {
      name
      id
    }
    ... on StixCyberObservable {
      __isStixCyberObservable: __typename
      id
      entity_type
      parent_types
      observable_value
      objectMarking {
        edges {
          node {
            id
            definition
          }
        }
      }
      objectLabel {
        edges {
          node {
            id
            value
            color
          }
        }
      }
    }
    ... on BasicRelationship {
      __isBasicRelationship: __typename
      id
      entity_type
      parent_types
    }
    ... on StixCoreRelationship {
      relationship_type
      id
    }
    ... on Artifact {
      id
    }
    ... on AutonomousSystem {
      id
    }
    ... on BankAccount {
      id
    }
    ... on CryptocurrencyWallet {
      id
    }
    ... on CryptographicKey {
      id
    }
    ... on Directory {
      id
    }
    ... on DomainName {
      id
    }
    ... on EmailAddr {
      id
    }
    ... on EmailMessage {
      id
    }
    ... on EmailMimePartType {
      id
    }
    ... on ExternalReference {
      id
    }
    ... on Hostname {
      id
    }
    ... on IPv4Addr {
      id
    }
    ... on IPv6Addr {
      id
    }
    ... on KillChainPhase {
      id
    }
    ... on Label {
      id
    }
    ... on MacAddr {
      id
    }
    ... on MarkingDefinition {
      id
    }
    ... on MediaContent {
      id
    }
    ... on Mutex {
      id
    }
    ... on NetworkTraffic {
      id
    }
    ... on Note {
      id
    }
    ... on ObservedData {
      id
    }
    ... on Opinion {
      id
    }
    ... on PaymentCard {
      id
    }
    ... on PhoneNumber {
      id
    }
    ... on Process {
      id
    }
    ... on Report {
      id
    }
    ... on Software {
      id
    }
    ... on StixCyberObservableRelationship {
      id
    }
    ... on StixFile {
      id
    }
    ... on StixMetaRelationship {
      id
    }
    ... on StixSightingRelationship {
      id
    }
    ... on Text {
      id
    }
    ... on Url {
      id
    }
    ... on UserAccount {
      id
    }
    ... on UserAgent {
      id
    }
    ... on WindowsRegistryKey {
      id
    }
    ... on WindowsRegistryValueType {
      id
    }
    ... on X509Certificate {
      id
    }
  }
  killChainPhases {
    edges {
      node {
        id
        phase_name
        x_opencti_order
      }
    }
  }
}

fragment SimpleStixObjectOrStixRelationshipStixCoreRelationshipsLines_data_3Yedex on Query {
  stixCoreRelationships(elementId: $elementId, relationship_type: $relationship_type, startTimeStart: $startTimeStart, startTimeStop: $startTimeStop, stopTimeStart: $stopTimeStart, stopTimeStop: $stopTimeStop, confidences: $confidences, orderBy: $orderBy, orderMode: $orderMode, first: $count, after: $cursor) {
    edges {
      node {
        ...SimpleStixObjectOrStixRelationshipStixCoreRelationshipLine_node
        id
        __typename
      }
      cursor
    }
    pageInfo {
      endCursor
      hasNextPage
    }
  }
}
'''
## just change i value
results = opencti_api_client.query(results = opencti_api_client.query(SimpleStixObjectOrStixRelationshipStixCoreRelationshipsLinesPaginationQuery,variables={"elementId":str(i),"relationship_type":"stix-core-relationship","orderBy":"created_at","orderMode":"desc","count":8})
print(results["data"]["stixCoreRelationships"]["edges"])
