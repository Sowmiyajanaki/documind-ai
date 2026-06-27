class SourceFormatter:
    """
    Formats retrieved document sources.
    """

    @staticmethod
    def format_sources(documents):

        sources = []

        seen = set()

        for doc in documents:

            page = doc.metadata.get("page_label")
            source = doc.metadata.get("source")

            key = (page, source)

            if key not in seen:
                seen.add(key)

                sources.append({
                    "page": page,
                    "source": source
                })

        return sources