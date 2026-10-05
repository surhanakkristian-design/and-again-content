// Lightweight Sentry store-API client for Edge Functions.
// Avoids pulling @sentry/deno into the Deno bundle. No request bodies —
// user photos and JWTs must never land in the event payload.

const DSN = Deno.env.get('SENTRY_DSN') ?? '';

interface ParsedDsn {
  protocol: string;
  key: string;
  host: string;
  projectId: string;
}

function parseDsn(dsn: string): ParsedDsn | null {
  try {
    const url = new URL(dsn);
    const key = url.username;
    const projectId = url.pathname.replace(/^\//, '').split('/')[0];
    if (!key || !projectId) return null;
    return {
      protocol: url.protocol.replace(':', ''),
      key,
      host: url.host,
      projectId,
    };
  } catch {
    return null;
  }
}

const parsed = DSN ? parseDsn(DSN) : null;

function eventId(): string {
  return crypto.randomUUID().replace(/-/g, '');
}

export async function captureEdgeException(
  error: unknown,
  context: { function: string; extra?: Record<string, unknown> },
): Promise<void> {
  if (!parsed) return;
  const err = error instanceof Error ? error : new Error(String(error ?? 'Unknown error'));
  const payload = {
    event_id: eventId(),
    timestamp: new Date().toISOString(),
    platform: 'javascript',
    logger: 'supabase-edge',
    environment: Deno.env.get('SENTRY_ENVIRONMENT') ?? 'production',
    server_name: 'supabase-edge',
    transaction: context.function,
    tags: {
      edge_function: context.function,
    },
    extra: context.extra ?? {},
    exception: {
      values: [
        {
          type: err.name,
          value: err.message,
        },
      ],
    },
  };
  try {
    await fetch(`${parsed.protocol}://${parsed.host}/api/${parsed.projectId}/store/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-Sentry-Auth': `Sentry sentry_version=7, sentry_client=4evr-edge/1.0, sentry_key=${parsed.key}`,
      },
      body: JSON.stringify(payload),
    });
  } catch (sendError) {
    console.error('sentry capture failed', sendError);
  }
}

export async function reportEdgeFailure(
  functionName: string,
  error: unknown,
  status: number,
): Promise<void> {
  if (status < 500) return;
  await captureEdgeException(error, { function: functionName });
}
