from ddtrace.span import Span
from ddtrace.internal.writer import TraceWriter

# writing to console so we can see the data is captured by Datadog.

class ConsoleWriter(TraceWriter):
    def recreate(self):
        # This method is required by the TraceWriter interface but can be left empty
        pass

    def stop(self, timeout=None):
        # This method is required by the TraceWriter interface but can be left empty
        pass

    def write(self, traces=None):
        # This method is called to write traces
        if traces:
            try:
                print("=" * 40)  # Separator for readability
                # Check if `traces` is a single Span object
                if isinstance(traces, list):
                    print("New Trace:")
                    for trace in traces:  # Iterate over traces (if it's a list)
                        if isinstance(trace, list):  # Handle a list of spans
                            for span in trace:
                                self._print_span(span)
                        elif isinstance(trace, Span):  # Handle a single span
                            self._print_span(trace)
                elif isinstance(traces, Span):  # Handle a single span directly
                    print("Single Span:")
                    self._print_span(traces)
                else:
                    print(f"Unexpected traces type: {type(traces)}")
                print("=" * 40)  # Separator for readability
            except Exception as e:
                print(f"Error dumping trace: {e}")


    def flush_queue(self):
        # This method is required by the TraceWriter interface but can be left empty
        pass

    def _print_span(self, span):
        """Helper method to print span details."""
        try:
            print(f"  Span Name: {span.name}")
            print(f"  Trace ID: {span.trace_id}")
            print(f"  Span ID: {span.span_id}")
            print(f"  Resource: {span.resource}")
            print(f"  Service: {span.service}")
            print("-" * 40)  # Separator for readability
        except Exception as e:
            print(f"Error printing span: {e}")
