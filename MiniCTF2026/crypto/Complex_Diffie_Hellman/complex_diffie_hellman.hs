import Data.Time
import Data.Ratio

-- All my constants (actual values hidden for security)
p :: Integer
gen :: Point
alicePrivate :: Integer
bobPrivate :: Integer


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
        putStrLn $ "Alice's public key " ++ (show alicePublic)
        putStrLn $ "Bob's public key " ++ (show bobPublic)
