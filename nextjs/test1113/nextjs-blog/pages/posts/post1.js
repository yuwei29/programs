import Link from 'next/link'
import Image from 'next/image'
import Head from 'next/head'
export default function FirstPost() {
  return <>
    <Head>
      <title>Post 1</title>
    </Head>
    <h1>First Post</h1>
    <h2>
        <Link href="/">Back to home</Link>
    </h2>
    <Image
    src="/images/t1.png" // Route of the image file
    height={1080} // Desired size with correct aspect ratio
    width={1920} // Desired size with correct aspect ratio
    alt="Your Name"
  />
  </>;
}

const img1 = () => (
  <Image
    src="/images/t1.png" // Route of the image file
    height={144} // Desired size with correct aspect ratio
    width={144} // Desired size with correct aspect ratio
    alt="Your Name"
  />
);