from performancetoday.models.episode import Episode

def graph_ql():
    from gql import gql, Client
    from gql.transport.aiohttp import AIOHTTPTransport

    # Select your transport with a defined url endpoint
    transport = AIOHTTPTransport(url="https://cmsapi.publicradio.org/graphql")

    # Create a GraphQL client using the defined transport
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # Provide a GraphQL query
    query = gql(
        """
        query CollectionQuery {
            collection(slug: "performance-today", contentAreaSlug: "yourclassical") {
                title
                subtitle
                canonicalSlug
                resourceType
                publishDate
                updatedAt
                descriptionText
                results(pageSize: 10 page: 1) {
                    totalPages
                    currentPage
                    nextPage
                    items {
                        title
                        subtitle
                        resourceType
                        publishDate
                        descriptionText
                        audio {
                         encodings {
                           filesize
                           format
                           httpFilePath
                         }
                         id
                         title
                         updatedAt
                        }
                        body
                        canonicalSlug
                        id
                        primaryVisuals {
                          thumbnail {
                            altText
                            caption
                            guid
                            type
                            preferredAspectRatio {
                              instances {
                                url
                                height
                                width
                              }
                              slug
                            }
                          }
                        }
                        ... on Link {
                            canonicalUrl
                            destination
                        }
                        ... on Episode {
                            episodeNumber
                            podcastBody
                        }
                        ... on Story {
                            shortTitle
                        }
                    }
                }
            }
        }
    """
    )

    # query = gql("""{
    #     __schema {
    #         types {
    #           name
    #         }
    #       }
    #   }""")

    query = gql("""
        {
          __type(name: "Program") {
            name
            description
            fields {
              name
              type {
                name
                kind
              }
            }
          }
        }
        """)
    # AudioList
    # Audio
    # Collection
    # CollectionItem
    # Episode
    # Image
    # Potlatch
    # Program
    # Segment
    # Story
    # query = gql("""{
    #         __schema {
    #             queryType {
    #               name
    #             }
    #           }
    #       }""")
    # Execute the query on the transport
    result = client.execute(query)
    import pprint
    pprint.pprint(result)


def main():

    import requests
    from bs4 import BeautifulSoup
    import json
    import pprint

    url = 'https://www.yourclassical.org/performance-today'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    Information = soup.find(id='__NEXT_DATA__').string
    y= json.loads(Information)
    #pprint.pprint(y['props']['pageProps']['data']['program']['results']['items'])
    episodes = y['props']['pageProps']['data']['program']['results']['items']
    for episode in episodes:
        title = episode['title']
        publishDate = episode['publishDate']
        description = episode['descriptionText']
        photoUrl = episode['primaryVisuals']['social']['preferredAspectRatio']['instances'][0]['url']
        audioUrl = episode['audio'][0]['encodings'][0]['playFilePath']
        e=Episode(publishDate, title, description, photoUrl, audioUrl)
        print(e)
    pass


if __name__ == '__main__':
    main()
