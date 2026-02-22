import Data.Time
import Data.Ratio

-- All my constants
p :: Integer
p = 275669402634072818971190768450467204123
gen = Point (2 % p)
alicePrivate :: Integer
alicePrivate = 97352983468190098626615526566666030569
bobPrivate :: Integer
bobPrivate = 260221482630310811718208640576980322575

-- We assume all points are on the unit circle, so r=1,
-- and we take every angle as a ratio of 2*pi*i
data Point = Point Rational
instance Show Point where
    show (Point x) = "1*e^(2*pi*i*(" ++ show x ++ "))"

reducePoint :: Point -> Point
reducePoint (Point p)
    | p >= 1 % 1 = reducePoint (Point (p - (1 % 1)))
    | otherwise  = Point p

generatePublicKey :: Point -> Integer -> Point
generatePublicKey (Point g) privateKey = Point (g * ratPrivateKey)
    where ratPrivateKey = toRational privateKey

generateSharedSecret :: Integer -> Point -> Point
generateSharedSecret myPrivateKey (Point theirPublicKey) = Point (ratPrivateKey * theirPublicKey)
    where ratPrivateKey = toRational myPrivateKey

reducedGeneratePublicKey :: Point -> Integer -> Point
reducedGeneratePublicKey p i = reducePoint (generatePublicKey p i)

reducedGenerateSharedSecret :: Integer -> Point -> Point
reducedGenerateSharedSecret i p = reducePoint (generateSharedSecret i p)

main :: IO ()
main =
    let
        -- Public key generation
        alicePublic = reducedGeneratePublicKey gen alicePrivate
        bobPublic = reducedGeneratePublicKey gen bobPrivate
        -- Alice sends A to Bob, Bob sends B to Alice
        aliceSharedSecret = reducedGenerateSharedSecret alicePrivate bobPublic
        bobSharedSecret = reducedGenerateSharedSecret bobPrivate alicePublic
    in do
        putStrLn $ "Alice's private key " ++ (show alicePrivate)
        putStrLn $ "Alice's public key " ++ (show alicePublic)
        putStrLn $ "Alice's copy of the shared key " ++ (show aliceSharedSecret)
        putStrLn $ "Bob's private key " ++ (show bobPrivate)
        putStrLn $ "Bob's public key " ++ (show bobPublic)
        putStrLn $ "Bob's copy of the shared key " ++ (show bobSharedSecret)

