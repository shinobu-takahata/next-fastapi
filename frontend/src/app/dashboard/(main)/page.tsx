import { ReactNode } from 'react';

export default function Page({ children }: { children: ReactNode }) {
    return (
        <div>
            <h1>Main Page</h1>
            {/* ここにメイン画面のコンテンツを追加 */}
        </div>
    );
}